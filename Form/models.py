from django.db import models
from Accounts.models import User
import Feedbacks

# Create your models here.

class Form(models.Model):
    choice_type = {
        'survey': 'Survey',
        'quiz': 'Quiz'
    }
    users_id = models.ForeignKey(User, on_delete=models.CASCADE,related_name='users')
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE,related_name='category')
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100,choices=choice_type)
    description = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    question = models.ForeignKey("Feedbacks.Question", on_delete=models.CASCADE,related_name='question')
    


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, primary_key=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)


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
