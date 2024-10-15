from django.db import models
from Accounts.models import User
from Form.models import Form

# Create your models here.

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='questions_user')
    form = models.ForeignKey(Form, on_delete=models.CASCADE,related_name='form_question')
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.body[:10]