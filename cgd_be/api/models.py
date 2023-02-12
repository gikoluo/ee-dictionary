from django.db import models

class Word(models.Model):
    WORD_TYPES = (
        ('noun', 'Noun'),
        ('verb', 'Verb'),
        ('adjective', 'Adjective'),
        ('adverb', 'Adverb'),
        ('preposition', 'Preposition'),
        ('conjunction', 'Conjunction'),
        ('interjection', 'Interjection'),
    )

    word = models.CharField(max_length=255)
    definition = models.TextField()
    language = models.CharField(max_length=255)
    part_of_speech = models.CharField(max_length=20, choices=WORD_TYPES)
    usage = models.TextField(blank=True)
    origin = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.word


class User(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
