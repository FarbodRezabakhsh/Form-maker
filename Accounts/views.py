from django.shortcuts import render
from rest_framework.views import APIView
from Accounts.models import User
from .serializers import UserSerializer,UserRegisterSerializer
from rest_framework.views import Response
from rest_framework import status

# Create your views here.

class UserListView(APIView):
    def get(self, request):
        users = User.objects.all()
        srz_data = UserSerializer(users,many=True)
        return Response(data=srz_data.data)



class UserRegisterView(APIView):
    def post(self, request):
        srz_data = UserRegisterSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.create(srz_data.validated_data)
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)