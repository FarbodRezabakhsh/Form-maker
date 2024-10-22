from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['email','phone_number','full_name','is_active']
    list_filter = ('is_admin',)
    search_fields = ('email','full_name')
    ordering = ('full_name',)

    fieldsets = [
        (None, {'fields':('email','phone_number','full_name','password')}),
        ('permission', {'fields':('is_active','is_admin','last_login')}),
    ]

admin.site.unregister(Group)

admin.site.register(User,UserAdmin)

