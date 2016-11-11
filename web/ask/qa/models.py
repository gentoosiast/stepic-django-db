from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    added_at = models.DateField()
    rating = models.IntegerField()
    author = models.ForeignKey(User)
    likes = models.ManyToManyField(User, related_name='likes_set')
    objects = QuestionManager()

class QuestionManager(models.Manager):
    def new(self):
        return self.order_by('-added_at')
    def popular(self):
        return self.order_by('-rating')

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField()
    question = OneToOneField(Question)
    author = models.ForeignKey(User)

