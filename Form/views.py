from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FormSerializer,CategorySerializer
from .models import Form,Category,Process
from rest_framework import status

# Create your views here.

class HomeView(APIView):
    def get(self,request):
        form = Form.objects.all()
        form_srz = FormSerializer(form,many=True)
        return Response(data=form_srz.data)


class FormCreateView(APIView):
    def post(self,request):
        srz_data = FormSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class FormUpdateView(APIView):
    def put(self,request,pk):
        form = Form.objects.get(pk=pk)
        srz_data = FormSerializer(instance=form,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_200_OK)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class FormDeleteView(APIView):
    def delete(self,request,pk):
        form = Form.objects.get(pk=pk)
        form.delete()
        return Response({'message':'Form deleted!'})

class CategoryListView(APIView):
    def get(self,request):
        category = Category.objects.all()
        srz_data = CategorySerializer(instance=category,many=True)
        return Response(data=srz_data.data)

class CategoryCreateView(APIView):
    def post(self,request):
        srz_data = CategorySerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdateView(APIView):
    def put(self,request,pk):
        category = Category.objects.get(pk=pk)
        ser_data = CategorySerializer(instance=category,data=category,partial=True)
        if ser_data.is_valid():
            ser_data.save()
            return Response(ser_data.data)
        return Response({'message':'you can not change form creator'})

class CategoryDeleteView(APIView):
    def delete(self,request,pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response({'message':'Category deleted!'})