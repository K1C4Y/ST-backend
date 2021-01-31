import pytest
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db

class TestAccountModels:

    def test_teacher_creation(self):
        obj = mixer.blend('accounts.Teacher')
        assert obj.pk == 1, 'Should save instance of teacher.'

    def test_student_creation(self):
        obj = mixer.blend('accounts.Student')
        assert obj.pk == 1, 'Should save instance of student.'

    def test_admin_creation(self):
        obj = mixer.blend('accounts.User')
        assert obj.pk == 1, 'Should save instance of User/admin)'

    def test_teacher_type(self):
        obj = mixer.blend('accounts.Teacher')
        assert obj.type == "TEACHER", 'Should be type TEACHER.'

    def test_student_type(self):
        obj = mixer.blend('accounts.Student')
        assert obj.type == "STUDENT", 'Should be type STUDENT.'

    def test_admin_typ(self):
        obj = mixer.blend('accounts.User')
        assert obj.type == "ADMIN", 'Should be type ADMIN.'
