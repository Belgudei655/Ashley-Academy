from django.db import models
from django.utils.crypto import get_random_string
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.contrib.admin.models import LogEntry
# Course DB

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Subject(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.course} - {self.name}"

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    yt_link = models.URLField()

    def __str__(self):
        return f"{self.subject} - {self.title}"

class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    test_question = models.TextField()
    answer1 = models.CharField(max_length=100)
    answer2 = models.CharField(max_length=100)
    answer3 = models.CharField(max_length=100)
    answer4 = models.CharField(max_length=100)
    correct_answer = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.lesson} - {self.test_question}"
    
#User side DB