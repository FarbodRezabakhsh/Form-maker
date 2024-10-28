from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FormSerializer,CategorySerializer
from .models import Form,Category,Process
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

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

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()

    def list(self,request):
        srz_data = CategorySerializer(instance=self.queryset,many=True)
        return Response(data=srz_data.data)

    def create(self, request):
        srz_data = CategorySerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        cat = get_object_or_404(self.queryset,pk=pk)
        srz_data = CategorySerializer(instance=cat)
        return Response(data=srz_data.data)

    def partial_update(self,request,pk):
        cat = get_object_or_404(self.queryset,pk=pk)
        srz_data = CategorySerializer(instance=cat,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_200_OK)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def destroy(self,request,pk):
        cat = get_object_or_404(self.queryset,pk=pk)
        cat.delete()
        return Response({'message':'category deleted'})
