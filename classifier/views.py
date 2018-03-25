from django.shortcuts import render, Http404
import en_core_web_sm as en
from .bcl import bcl
import os
from .forms import UploadFileForm
from django.conf import settings
from django.http import HttpResponse
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn.svm import LinearSVC
nlp = en.load()


def overlapping(question):
    # Open File and Select Sheet
    f = 'media/training/overlapping.xlsx'
    sheet = pd.ExcelFile(f)
    df_train = sheet.parse("Sheet2")

    def training(df_train):
        label_encoding = preprocessing.LabelEncoder()
        df_train['CategoryLabel'] = label_encoding.fit_transform(df_train['Category'])
        question_train = df_train['Question']
        category_train = df_train['CategoryLabel']
        vectorizer = CountVectorizer()
        # Training Set
        x_train = vectorizer.fit_transform(question_train).toarray()
        y_train = list(category_train)
        # Linear SVC
        clf = LinearSVC()
        clf.fit(x_train, y_train)
        return vectorizer, clf, label_encoding

    def testing(question, vectorizer, clf, label_encoding):
        x_test = vectorizer.transform(question)
        y_test = clf.predict(x_test)
        category = label_encoding.inverse_transform(y_test)
        return str(category[0])

    vectorizer, clf, label_encoding = training(df_train)
    output_category = testing(question, vectorizer, clf, label_encoding)
    return output_category


def find_category(question):
    verb_category_list = []
    count = 0
    question_copy = question
    question = nlp(unicode(question, "utf-8"))
    for token in question:
        if str(token.text).lower() in bcl.wh_questions:
            return "Understanding"
        if token.tag_=='VB' or token.tag_ == "WDT" or token.tag_ == "WP" or token.tag_ == "WP$" or token.tag_ == "WRB":
            verb = str(token.text)
            for b in bcl.bloom:
                if verb.lower() in b:
                    verb_category_list.append(bcl.level[str(count)])
                count = count + 1
    if len(verb_category_list) == 0:
        return "Verb Does Not Exist In List"
    elif len(verb_category_list) == 1:
        return verb_category_list[0]
    else:
        return overlapping([question_copy])


def index1(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            upload_file_form.save()
            uploaded_file = open("media/"+str(request.FILES['file']), "r")
            question_list = [question for question in uploaded_file.read().split("\n") if len(question) > 0]
            output_file = open("media/output.csv", "w")
            for i in range(0, len(question_list)):
                category = find_category(question_list[i])
                """question = nlp(unicode(question_list[i], "utf-8"))
                for token in question:
                    if str(token.text).lower() in bcl.wh_questions:
                        category = "Understanding"
                        break
                    if str(token.tag_) == "VB":
                        verb = str(token.text)
                        category = find_category(str(question))
                        break"""
                output_file.write("\"" + str(question_list[i]) + "\"" + "," + str(category) + "\n")
            return render(request, 'classifier/result1.html', {'output_file': download("output.csv")})
    else:
        upload_file_form = UploadFileForm()
        return render(request, 'classifier/index1.html', {'form': upload_file_form})


def download(path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            print(file_path)
            return file_path
    raise Http404


"""
def result1(request):
    return render(request, 'classifier/result1.html')


def result1(request):
    if request.method == 'POST':
        my_file = request.FILES['my_file']
        file_content = str(my_file.read())
        file_content = file_content.rsplit("\n")
        output_file = open("output.csv","w")
        nlp = en.load()
        for i in range(0, len(file_content)):
            question = nlp(unicode(str(question), "utf-8"))
            for token in question:
                if str(token.tag_) == "VB":
                    verb = str(token.text)
                    category = find_category(verb)
                    break
            output_file.write(question_copy + "," + str(category) + "\n")
        output_file.close()
        return render(request, 'classifier/result1.html')
"""


def index(request):
    return render(request, 'classifier/index.html')


def result(request):
    input_question = str(request.POST.get('input_question', None))
    question = nlp(unicode(input_question, "utf-8"))
    for token in question:
        if token.tag_ == "VB":
            verb = token.text
            category = find_category(verb)
            break
    return render(request, 'classifier/result.html', {'verb': verb, 'category': category})

