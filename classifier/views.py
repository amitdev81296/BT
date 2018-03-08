from django.shortcuts import render, redirect, Http404
import en_core_web_sm as en
from .bcl import bcl
import os
from .forms import UploadFileForm
from django.conf import settings
from django.http import HttpResponse
nlp = en.load()


def find_category(verb):
    verb_category_list = []
    count = 0
    for b in bcl.bloom:
        if verb.lower() in b:
            verb_category_list.append(bcl.level[str(count)])
        count = count + 1
    if len(verb_category_list) == 0:
        return "Verb Does Not Exist In List"
    elif len(verb_category_list) == 1:
        return verb_category_list[0]
    else:
        return "Overlapping"


def index1(request):
    if request.method == 'POST':
        upload_file_form = UploadFileForm(request.POST, request.FILES)
        if upload_file_form.is_valid():
            upload_file_form.save()
            uploaded_file = open("media/"+str(request.FILES['file']), "r")
            question_list = uploaded_file.read().split("\n")
            output_file = open("media/output.csv", "w")
            del question_list[-1]
            for i in range(0, len(question_list)):
                question = nlp(unicode(question_list[i], "utf-8"))
                for token in question:
                    if str(token.text).lower() in bcl.wh_questions:
                        category = "Understanding"
                        break
                    if str(token.tag_) == "VB":
                        verb = str(token.text)
                        category = find_category(verb)
                        break
                output_file.write("\"" + str(question) + "\"" + "," + str(category) + "\n")
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
    nlp = en.load()
    question = nlp(unicode(input_question, "utf-8"))
    for token in question:
        if token.tag_ == "VB":
            verb = token.text
            category = find_category(verb)
            break
    return render(request, 'classifier/result.html', {'verb': verb, 'category': category})

