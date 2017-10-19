from django.shortcuts import render
from .models import Verb
# from django.http import HttpResponse
import nltk
from .bcl import bcl
nltk.download('punkt')


def find_category(verb):
    count = 0
    for b in bcl.bloom:
        if verb.lower() in b:
            return bcl.level[str(count)]
        count = count + 1


def index(request):
    return render(request, 'classifier/index.html')


def result(request):
    input_question = str(request.POST.get('input_question', None))
    tokens = nltk.word_tokenize(input_question)
    tagged = nltk.pos_tag(tokens)
    for t in tagged:
        if t[1] == 'VB':
            verb = t[0]
            category = find_category(t[0])
            break

    return render(request, 'classifier/result.html', {'verb': verb, 'category': category})
