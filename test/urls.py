from django.urls import path
from .views import TestList, TestDetail, TestAnswerList,TestAnswerDetail 


app_name = 'tests'

urlpatterns = [
    path('tests/',TestList.as_view(), name ='tests'),
    path('tests/<int:pk>',TestDetail.as_view(), name ='test'),
    path('testanswers/',TestAnswerList.as_view(), name ='testanswers'),
    path('testanswers/<int:pk>',TestAnswerDetail.as_view(), name ='testanswer'),
]
