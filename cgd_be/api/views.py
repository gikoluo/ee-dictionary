from django.shortcuts import render

from django.http import JsonResponse
from api.models import Word

def word_list(request):
    words = Word.objects.all()
    word_list = [{'word': word.word, 'definition': word.definition, 'usage': word.usage, 'origin': word.origin} for word in words]
    return JsonResponse(word_list, safe=False)