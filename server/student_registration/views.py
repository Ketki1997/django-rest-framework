from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view,authentication_classes,permission_classes
# from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import UserSerializer,StudentSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Student
from django.utils.decorators import method_decorator
from .middlewares  import current_user_middleware
from .tokens import StudentAccessToken

@api_view(['POST'])
def login(request):
    student = authenticate(request,username=request.data['username'], password=request.data['password'])
    if student is not None:
        user = User.objects.get(username=request.data['username'])
        refresh = RefreshToken.for_user(user)
        access_token = str(refresh.access_token)
        serializer = UserSerializer(instance= user)
        return Response({'token':access_token,"user": serializer.data})
    else:
        return Response({"detail": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
    

@api_view(['POST'])
def signup(request):
    # check if username already exists
    username = request.data.get('username')
    if User.objects.filter(username=username).exists():
        return Response({'error':'Username already exists'},status=status.HTTP_400_BAD_REQUEST)
    # afterchecking if username dosent exist make student registration 
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        # token = Token.objects.create(user=user)
        return Response({"message": "Registration successfull.","user":serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def token(request):
    return Response("Passed for {}".format(request.user.email))


#student registration
@api_view(['POST'])
def student_registration(request):
    username = request.data.get('username')
    if Student.objects.filter(username = username).exists():
        return Response({'error':'Username already exists'},status=status.HTTP_400_BAD_REQUEST)
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        hashed_password = make_password(request.data['password'])
        serializer.validated_data['password'] = hashed_password
        serializer.save()
        return Response({"message": "Registration successfull.","student":serializer.data}, status=status.HTTP_200_OK)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# student login
@api_view(['POST'])
def student_login(request):
    username = request.data.get('username')
    try:
        student = Student.objects.get(username=username)
    except Student.DoesNotExist:
        return Response({'error':'Student not found'},status=status.HTTP_404_NOT_FOUND)
    if check_password(request.data['password'],student.password):
        refresh = RefreshToken.for_user(student)
        access_token = str(refresh.access_token)
        serializer = StudentSerializer(student)
        student_data = serializer.data
        student_data['access_token'] = access_token
        student_data['refresh_token'] = str(refresh)
        return Response({'message': 'Login successful', 'student': student_data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

    
#get the student listing with authentication
@api_view(['GET'])
@current_user_middleware
def student_listing(request):
    print(request.user)
    student = Student.objects.all()
    student_list = list(student.values())
    return Response({'students-list' :student_list }, status=status.HTTP_200_OK)


# update the registered student
@api_view(['PUT'])
@current_user_middleware
def student_update(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'message' : f'Student with ID {student_id} does not exist' }, status=status.HTTP_400_BAD_REQUEST)
    studentdata = StudentSerializer(instance=student, data=request.data, partial=True)
    if studentdata.is_valid():
        studentdata.save()
        return Response({'message' :"Student data updated successfully" }, status=status.HTTP_200_OK)
    else:
        return Response({'message' :"Student is Invalid",'errors':studentdata.errors }, status=status.HTTP_200_OK)
    
# delete the registered student with authentication
@api_view(['DELETE'])
@current_user_middleware
def student_delete(request,student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return Response({'message' : f'Student with ID {student_id} does not exist' }, status=status.HTTP_400_BAD_REQUEST)
    student.delete()
    return Response({'message' :"Student data deleted successfully" }, status=status.HTTP_200_OK)
