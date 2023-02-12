# api/urls.py

from django.urls import path
from .views import WordList

urlpatterns = [
    path('words/', WordList.as_view(), name='word-list'),
]
