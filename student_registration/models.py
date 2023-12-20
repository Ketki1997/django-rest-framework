from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 15)
    