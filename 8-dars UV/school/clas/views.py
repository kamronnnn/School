from django.shortcuts import render
from .serializers import CLasSerializer, TeacherSerializer, StudentSerializer
from .models import Clas, Teacher, Student
from rest_framework import viewsets

# Create your views here.


class ClasList(viewsets.ModelViewSet):
    queryset = Clas.objects.all()
    serializer_class = CLasSerializer


class TeacherList(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



