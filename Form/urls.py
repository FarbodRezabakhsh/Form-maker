
from . import views
from django.urls import path
from rest_framework import routers
from .views import CategoryViewSet, QuestionViewSet

app_name = 'Form'
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('create/',views.FormCreateView.as_view()),
    path('update/<int:pk>/',views.FormUpdateView.as_view()),
    path('delete/<int:pk>/',views.FormDeleteView.as_view()),
]

router = routers.SimpleRouter()
router.register('category',CategoryViewSet)
router.register('questions',QuestionViewSet)
urlpatterns += router.urls