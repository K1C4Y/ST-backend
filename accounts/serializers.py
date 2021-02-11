from rest_framework import serializers
from .models import Student, Teacher, User
from test.models import Test, TestAnswer 
from rest_framework.authtoken.models import Token

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

class StudentCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['username', 'password', 'email']

class TeacherCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['username', 'password', 'email']

class TokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Token
        fields = ['key']
