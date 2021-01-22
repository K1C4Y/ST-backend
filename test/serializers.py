from rest_framework import serializers
from .models import *
from accounts.models import Teacher, Student
from accounts.serializers import StudentSerializer, TeacherSerializer

#First serializers related to test model:
class TestSerializer(serializers.ModelSerializer):
    teacher = serializers.ModelField(model_field=Teacher.username)
    tests = serializers.PrimaryKeyRelatedField(many=True, queryset=TestAnswer.objects.all())
    openQuestions = serializers.PrimaryKeyRelatedField(many=True, queryset=OpenQuestion.objects.all())
    closedQuestions = serializers.PrimaryKeyRelatedField(many=True, queryset=ClosedQuestion.objects.all())

    class Meta:
        model = Test
        fields = ['teacher','title','KeyCode','datePublished', 'openQuestions', 'closedQuestions']


class OpenQuestionSerializer(serializers.ModelSerializer):
    test = serializers.ModelField(model_field=Test.title)

    class Meta:
        model = OpenQuestion
        fields = ['question','test']


class ClosedQuestionSerializer(serializers.ModelSerializer):
    test = serializers.ModelField(model_field=Test.title)
    answers = serializers.PrimaryKeyRelatedField(many=True, queryset=Answer.objects.all())

    class Meta:
        model = ClosedQuestion
        fields = ['question','test','answers']


class AnswerSerializer(serializers.ModelSerializer):
    closedquestion = serializers.ModelField(model_field=Test.title)

    class Meta:
        model = OpenQuestion
        fields = ['closedquestion','answer']


#Here TestAnswer seriallizers start

class TestAnswerSerializer(serializers.ModelSerializer):
    student = serializers.ModelField(model_field=Student.username)
    test = serializers.ModelField(model_field=Test.title)
    cqanswers = serializers.PrimaryKeyRelatedField(many=True, queryset=CQAnswer.objects.all())
    oqanswers = serializers.PrimaryKeyRelatedField(many=True, queryset=OQAnswer.objects.all())

    class Meta:
        model = TestAnswer
        fields = ['student', 'test','datePublished','dateGraded', 'cqanswers', 'oqanswers']


class CQAnswerSerializer(serializers.ModelSerializer):
    testAnswer = serializers.ModelField(model_field=TestAnswer.id)

    class Meta:
        model = ClosedQuestion
        fields = ['testanswer','answer']


class OQAnswerSerializer(serializers.ModelSerializer):
    testAnswer = serializers.ModelField(model_field=TestAnswer.id)

    class Meta:
        model = ClosedQuestion
        fields = ['testanswer','answer']


