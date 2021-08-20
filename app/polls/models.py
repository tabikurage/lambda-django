import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_id = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text
    """
    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    """
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        
        
class Result(models.Model):
    card_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.card_name
        
class Choice(models.Model):
    # related_name='choice_set'はデフォルト値のため、無くても動く
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choice_set')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    next_questions = models.ManyToManyField(Question, related_name='previous_choices',blank=True)
    result = models.ForeignKey(Result, null=True, blank=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.choice_text
