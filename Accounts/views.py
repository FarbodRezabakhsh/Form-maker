from django.shortcuts import render
from rest_framework.views import APIView
from Accounts.models import User
from .serializers import UserSerializer
from rest_framework.views import Response


# Create your views here.


class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = UserSerializer(users,many=True)
        return Response(data=srz_data.data)

class UserRegisterView(APIView):
    def post(self, request):
        pass
