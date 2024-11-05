

from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'accounts'
urlpatterns = [
    path('',views.UserListView.as_view(),name='user_list'),
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

'''
{
	"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMDQwMzgyNywiaWF0IjoxNzMwMzE3NDI3LCJqdGkiOiIwNzdhMThhNzQ1OGQ0Yjk5OGI0NGVmNDVjYmU5NzgxYiIsInVzZXJfaWQiOjF9.0crbYsgHv_HDVIR0N_D34__MKMuVNJhcRMQyG_HkDZI",
	"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMwMzE3NzI3LCJpYXQiOjE3MzAzMTc0MjcsImp0aSI6ImUxZmYxOGQ2NzgzZDQzNjU5Mzk5NzM1NGYyOTI4YzIyIiwidXNlcl9pZCI6MX0.muyAI_cSDq-_cICe3PbTPz09PUoM7cPfjaa2dSsW9tY"
}
'''