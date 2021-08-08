from task_app.models import Word
from task_app.serializers import WordSerializer
from rest_framework import viewsets
from django.shortcuts import render
from django.http import HttpResponse
import json
import logging
logger = logging.getLogger('django')

class WordViewSet(viewsets.ModelViewSet):
    queryset = Word.objects.all()
    serializer_class = WordSerializer

def words(request):
    words = []
    state_name = request.GET.get('digit', None)
    all_words = Word.objects.all().values('name')
    words = getWords(state_name, all_words)
    words.sort()
    jsonWords = json.dumps(words)
    return HttpResponse(json.dumps(words), content_type = "application/json")

def getWords(digit, all_words):
    wanted_letters = len(digit)
    result = []
    for word in all_words:
        now_word = word['name']
        word_length = len(now_word)
        if word_length == wanted_letters:
            c = rightWords(now_word, digit)
            if c != 0:
                result.append(now_word)
    return result

def rightWords(word, wanted_letters):
    c = 0
    length = -1
    for letter in word:
        length = length + 1
        digit = wanted_letters[length]
        if letter == "a" or letter == "b" or letter == "c":
            dig = 2
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "d" or letter == "e" or letter == "f":
            dig = 3
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "g" or letter == "h" or letter == "i":
            dig = 4
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "j" or letter == "k" or letter == "l":
            dig = 5
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "m" or letter == "n" or letter == "o":
            dig = 6
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "p" or letter == "q" or letter == "r" or letter == "s":
            dig = 7
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "t" or letter == "u" or letter == "w":
            dig = 8
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
        elif letter == "w" or letter == "x" or letter == "y" or letter == "z":
            dig = 9
            if str(dig) == digit:
                c = 1 
            else:
                c = 0
                break
    return c
