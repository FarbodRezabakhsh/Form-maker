
from rest_framework import serializers
from .models import Form, Category, Process, Question


class FormSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Form
        fields = ['id','user','category','title','type','description','is_private','questions']

    def get_questions(self, obj):
        result = obj.questions.all()
        return QuestionSerializers(instance=result, many=True).data


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name','form']

class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'