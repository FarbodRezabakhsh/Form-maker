from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FormSerializer,CategorySerializer,QuestionSerializers
from .models import Form,Category,Process,Question
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from permissions import IsOwnerOrReadOnly
from rest_framework.decorators import permission_classes
from rest_framework.throttling import  UserRateThrottle,AnonRateThrottle
from rest_framework.decorators import throttle_classes

# Create your views here.

class HomeView(APIView):
    """
        Listing all forms
    """
    throttle_classes = [AnonRateThrottle]
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializers
    def get(self,request):
        form = Form.objects.all()
        form_srz = self.serializer_class(form,many=True)
        return Response(data=form_srz.data)


class FormCreateView(APIView):
    """
        Creating new forms
    """
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializers
    def post(self,request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class FormUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = QuestionSerializers
    def put(self,request,pk):
        form = Form.objects.get(pk=pk)
        self.check_object_permissions(request,form)
        srz_data = self.serializer_class(instance=form,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_200_OK)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class FormDeleteView(APIView):
    permission_classes = [IsAuthenticated,IsOwnerOrReadOnly]
    serializer_class = QuestionSerializers
    def delete(self,request,pk):
        form = Form.objects.get(pk=pk)
        self.check_object_permissions(request,form)
        form.delete()
        return Response({'message':'Form deleted!'})

class CategoryViewSet(viewsets.ViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]

    @throttle_classes([AnonRateThrottle])
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
        cat = get_object_or_404(Category,pk=pk)
        self.permission_classes = [IsOwnerOrReadOnly]
        self.check_object_permissions(request,cat)
        srz_data = CategorySerializer(instance=cat,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_200_OK)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk):
        cat = get_object_or_404(self.queryset,pk=pk)
        self.permission_classes = [IsOwnerOrReadOnly]
        self.check_object_permissions(request,cat)
        cat.delete()
        return Response({'message':'category deleted'})


class QuestionViewSet(viewsets.ViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializers

    def list(self,request):
        srz_data = self.serializer_class(instance=self.queryset, many=True)
        self.throttle_classes = [AnonRateThrottle]
        return Response(srz_data.data,status=status.HTTP_200_OK)

    def create(self,request):
        srz_data = self.serializer_class(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data,status=status.HTTP_201_CREATED)
        return Response(data=srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk):
        question = get_object_or_404(self.queryset,pk=pk)
        srz_data = self.serializer_class(instance=question)
        return Response(srz_data.data,status=status.HTTP_200_OK)


    def partial_update(self,request,pk):
        question = get_object_or_404(Question,pk=pk)
        self.permission_classes = [IsOwnerOrReadOnly]
        self.check_object_permissions(request,question)
        srz_data = self.serializer_class(instance=question,data=request.data,partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


    def destroy(self,request,pk):
        question = get_object_or_404(Question,pk=pk)
        self.permission_classes = [IsOwnerOrReadOnly]
        self.check_object_permissions(request, question)
        self.check_object_permissions(request,question)
        question.delete()
        return Response({'message':'question deleted'})