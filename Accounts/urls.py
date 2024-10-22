

from django.urls import path,include
from . import views
from rest_framework.authtoken import views as auth_token


app_name = 'accounts'
urlpatterns = [
    path('',views.UserListView.as_view(),name='user_list'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('api-token-auth/', auth_token.obtain_auth_token)
]
