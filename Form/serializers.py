
from rest_framework import serializers
from .models import Form, Category, Process, Question


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id','user','category','title','type','description','is_private']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','form']

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'