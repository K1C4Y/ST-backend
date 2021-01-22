from django.db import models
from accounts.models import Teacher, Student

# Teacher Tests

class Test(models.Model):
    teacher = models.ForeignKey(Teacher, related_name='tests', on_delete=models.CASCADE) 
    title = models.CharField(max_length=50)
    KeyCode = models.CharField(max_length=50)
    datePublished = models.DateTimeField(auto_now_add=True)
    dateToGive = models.DateTimeField()
   
class OpenQuestion(models.Model):
    test = models.ForeignKey(Test, related_name='openQuestions', on_delete=models.CASCADE)
    question = models.TextField()

class ClosedQuestion(models.Model):
    test = models.ForeignKey(Test, related_name='closedQuestions', on_delete=models.CASCADE)
    question = models.TextField()
    correct = models.IntegerField()

class Answer(models.Model):
    question = models.ForeignKey(ClosedQuestion, related_name='answers', on_delete=models.CASCADE)
    answer = models.TextField()


# Student Test

class TestAnswer(models.Model):
    student = models.ForeignKey(Student, related_name='testAnswers', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='testAnswers', on_delete=models.CASCADE, default=1)
    datePublished = models.DateTimeField(auto_now_add=True)
    dateGraded = models.DateTimeField()

class CQAnswer(models.Model):
    answer = models.IntegerField()
    testAnswer = models.ForeignKey(TestAnswer, related_name='CQAnswers', on_delete=models.CASCADE)

class OQAnswer(models.Model):
    answer = models.TextField()
    testAnswer = models.ForeignKey(TestAnswer, related_name='OQAnswers', on_delete=models.CASCADE)

