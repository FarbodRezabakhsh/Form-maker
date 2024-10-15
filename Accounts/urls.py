

from django.urls import path,include
from . import views


app_name = 'accounts'
urlpatterns = [
    path('',views.UserListView.as_view(),name='user_list'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
]
