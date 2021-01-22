from rest_framework import generics
from .models import Student, Teacher
from .serializers import TeacherSerializer, StudentSerializer 
from rest_framework import permissions
# Create your views here.

class TeacherList(generics.ListAPIView):
    queryset= Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherDetail(generics.RetrieveAPIView):
    queryset= Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentList(generics.ListAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveAPIView):
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

class TeacherCreate(generics.CreateAPIView):
    queryset=Student.objects.all()
    serializer_class = TeacherSerializer
    premission_classes = [permissions]
