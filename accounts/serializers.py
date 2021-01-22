from rest_framework import serializers
from djoser.serializers import UserCreateSerializer 
from .models import Student, Teacher, User
from test.models import Test, TestAnswer 

class TeacherSerializer(serializers.ModelSerializer):
    tests = serializers.PrimaryKeyRelatedField(many=True, queryset=Test.objects.all())

    class Meta:
        model = Teacher
        fields = ['id', 'username', 'tests']


class StudentSerializer(serializers.ModelSerializer):
    testAnswers = serializers.PrimaryKeyRelatedField(many=True, queryset=TestAnswer.objects.all())

    class Meta:
        model = Student
        fields = ['id', 'username', 'testAnswers']


class UserCreation(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['username', 'password']

