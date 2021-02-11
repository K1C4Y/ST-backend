from rest_framework import generics, status
from .models import Student, Teacher
from .serializers import *
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class TeacherList(generics.ListAPIView):
    queryset= Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveAPIView):
    queryset= Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherCreate(generics.CreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class = TeacherCreateSerializer

class StudentList(generics.ListAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class StudentCreate(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class = StudentCreateSerializer

class StudentLogin(APIView):
    def post(self,request):
        data = request.data
        try:
            student = Student.objects.filter(username=data["username"])
        except:
            return Response(data,status=status.HTTP_404_NOT_FOUND)

        student = student[0]

        if student.password==data["password"]:
            try:
                Token.objects.create(user=student)
            except:
                pass
            try:
                token = Token.objects.filter(user=student)
            except:
                return Response("No aviable token.", status=status.HTTP_404_NOT_FOUND)

            token = token[0]
            token = TokenSerializer(token)
            return Response(token.data["key"])

        return Response(data,status= status.HTTP_500_INTERNAL_SERVER_ERROR)

class TeacherLogin(APIView):
    def post(self,request):
        data = request.data
        try:
            teacher = Teacher.objects.filter(username=data["username"])
        except:
            return Response(data.username,status=status.HTTP_404_NOT_FOUND)

        teacher = teacher[0]

        if teacher.password==data["password"]:
            try:
                Token.objects.create(user=teacher)
            except:
                pass
            try:
                token = Token.objects.filter(user=teacher)
            except:
                return Response("No aviable token.", status=status.HTTP_404_NOT_FOUND)

            token = token[0]
            token = TokenSerializer(token)
            return Response(token.data["key"])

        return Response(data,status= status.HTTP_500_INTERNAL_SERVER_ERROR)

