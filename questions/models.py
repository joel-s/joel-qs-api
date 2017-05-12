from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    distractors = models.CharField(max_length=255)
