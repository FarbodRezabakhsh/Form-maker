from . import views
from django.urls import path



app_name = 'Form'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
]

