from django.db import models
from Accounts.models import User
import Feedbacks



class Form(models.Model):
    choice_type = {
        'survey': 'Survey',
        'quiz': 'Quiz'
    }
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users')
    category = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='category',blank=True, null=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=choice_type)
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)


class Question(models.Model):
    choice_type = (
        ('text', 'Text'),
        ('multiple_choice', 'Multiple Choice'),
        ('checkbox', 'Checkbox'),
        ('rating', 'Rating'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users_question')
    title = models.CharField(max_length=100)
    question_type = models.CharField(max_length=100,choices=choice_type)
    required = models.BooleanField(default=False)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE,related_name='form_category')


class Process(models.Model):
    PROCESS_TYPE_CHOICES = (
        ('public', 'Public'),
        ('personal', 'Personal'),
    )
    name = models.CharField(max_length=255)
    process_type = models.CharField(max_length=10, choices=PROCESS_TYPE_CHOICES)
    is_linear = models.BooleanField(default=True)
    forms = models.ManyToManyField(Form)
    password = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name
