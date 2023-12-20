from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['fullname','username','password','mobile']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']