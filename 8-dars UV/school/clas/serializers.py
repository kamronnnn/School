from rest_framework import serializers
from .models import Clas, Teacher, Student


class CLasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clas
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
