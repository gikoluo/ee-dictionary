# api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Word
from .serializers import WordSerializer

class WordList(APIView):
    def get(self, request, format=None):
        words = Word.objects.all()
        serializer = WordSerializer(words, many=True)
        return Response(serializer.data)
