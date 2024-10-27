from . import views
from django.urls import path



app_name = 'Form'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('create/',views.FormCreateView.as_view()),
    path('update/<int:pk>/',views.FormUpdateView.as_view()),
    path('delete/<int:pk>/',views.FormDeleteView.as_view()),
    path('category/',views.CategoryListView.as_view()),
    path('category/create/',views.CategoryCreateView.as_view()),
]

