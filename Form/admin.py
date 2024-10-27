from django.contrib import admin

from Form.models import Form,Category


# Register your models here.

class FormAdmin(admin.ModelAdmin):
    list_display = ('title','type','user','category')
    search_fields = ('title',)


admin.site.register(Form, FormAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','form']
    list_filter = ('form',)

admin.site.register(Category,CategoryAdmin)