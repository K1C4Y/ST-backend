from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework import permissions

from accounts.models import Teacher, Student
from .models import Test, TestAnswer
from .serializers import TestSerializer, TestAnswerSerializer
from .permissions import IsTeacherOrReadOnly, IsStudentOrReadOnly

class TestList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.teacher)

class TestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsTeacherOrReadOnly]

class TestAnswerList(generics.ListCreateAPIView):
    queryset = Test.objects.all()
    serializer_class = TestAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsStudentOrReadOnly,IsTeacherOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.student)

class TestAnswerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TestAnswer.objects.all()
    serializer_class = TestAnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsStudentOrReadOnly,IsTeacherOrReadOnly]
