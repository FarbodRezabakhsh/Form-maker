from django.contrib import admin

from Form.models import Form, Category, Question


# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display = ('title','type','user','category')
    search_fields = ('title',)

admin.site.register(Form, FormAdmin)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('user','form','title')
    search_fields = ('title',)
    list_filter = ('user','form','question_type')

admin.site.register(Question, QuestionAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','form']
    list_filter = ('form',)

admin.site.register(Category,CategoryAdmin)