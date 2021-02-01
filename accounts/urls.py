from django.urls import path, include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('teachers/',TeacherList.as_view(), name ='teachers'),
    path('teacher/<int:pk>',TeacherDetail.as_view(), name ='teacher'),
    path('teacher/create/', TeacherCreate.as_view(), name='teacherCreate'),
    path('student/create/', StudentCreate.as_view(), name='studentCreate'),
    path('students/',StudentList.as_view(), name ='students'),
    path('student/<int:pk>',StudentDetail.as_view(), name ='student'),
]
