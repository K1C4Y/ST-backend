import pytest
from rest_framework.authtoken.models import Token
from accounts import views 
from accounts.models import Student, Teacher
from mixer.backend.django import mixer
from rest_framework.test import APIRequestFactory
from rest_framework.authtoken.views import obtain_auth_token

pytestmark = pytest.mark.django_db

class TestAccountViews:

    arf = APIRequestFactory()

    username = "Mary"
    password = "secreto1"
    email = "Mary1@email.com"

    def test_get_teacher(self):
        teacher = mixer.blend('accounts.Teacher')
        req = self.arf.get('/')
        resp = views.TeacherDetail.as_view()(req,pk=teacher.pk)
        assert resp.status_code == 200, 'Schould be callable with no login.'

    def test_get_student(self):
        student = mixer.blend('accounts.Student')
        req = self.arf.get('/')
        resp = views.StudentDetail.as_view()(req,pk=student.pk)
        assert resp.status_code == 200, 'Schould be callable with no login.'

    def test_teacher_create(self):
        req = self.arf.post('/', {"username":self.username,"password":self.password, "email":self.email})
        resp = views.TeacherCreate.as_view()(req)
        assert resp.status_code == 201, 'Everyone should create Teacher.'

    def test_student_create(self):
        req = self.arf.post('/', {"username":self.username,"password":self.password, "email":self.email})
        resp = views.TeacherCreate.as_view()(req)
        assert resp.status_code == 201, 'Everyone should  create Teacher.'

    def test_student_login(self):
        student = mixer.blend("accounts.Student",username = "Mary",password="secreto1")
        student.save()
        req = self.arf.post('/',{"username":"Mary", "password":"secreto1"})
        resp = views.StudentLogin.as_view()(req)
        assert resp.status_code == 200, "Should login Teacher"
        assert type(resp.data) == str

    def test_teacher_login(self):
        teacher = mixer.blend("accounts.Teacher",username = "Mary",password="secreto1")
        teacher.save()
        req = self.arf.post('/',{"username":"Mary", "password":"secreto1"})
        resp = views.TeacherLogin.as_view()(req)
        assert type(resp.data) == str
        assert resp.status_code == 200, "Should login Student"

