from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['email','phone_number','full_name','is_active']

admin.site.register(User)
