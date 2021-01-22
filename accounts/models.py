from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
# Create your models here.

class User(AbstractUser):
    class Types(models.TextChoices):
        Teacher = "TEACHER", "Teacher"
        Student = "STUDENT", "Student"
        Admin = "ADMIN", "Admin"
    
    base_type= Types.Admin

    type = models.CharField(_("Type"), max_length=50, choices=Types.choices, default=base_type)

    REQUIRED_FIELDS=['type']

    def get_absolute_url(self):
        return reverse("user:detail", kwargs={"username":self.username})

    def save(self, *args, **kwargs):
        if not self.id:
            self.type = self.base_type
        return super().save(*args, **kwargs)


class TeacherManager(models.Manager):

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Teacher)

class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(type=User.Types.Student)

class Student(User):
    base_type = User.Types.Student
    objects = StudentManager()
    
    class Meta:
        proxy = True

class Teacher(User):
    base_type = User.Types.Teacher
    objects = TeacherManager()

    class Meta:
        proxy = True

