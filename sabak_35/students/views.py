from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Student
from .serializers import StudentCreateSerializer, StudentSerializer
# Create your views here.

def hello_world(request):
    return HttpResponse("Hello_world")

@api_view(['GET'])
def students_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def student_add(request):

    serializer = StudentCreateSerializer(data=request.data)

    if serializer.is_valid():
        student = serializer.save()

        serializer2 = StudentSerializer(student)

        return Response(serializer2.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['PATCH'])
def student_update(request, id):
    
    try:
        student = Student.objects.get(id=id)

    except Student.DoesNotExist:
        return Response({"errors": "Student tabylbady"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentCreateSerializer(student, data=request.data, partial=True)

    if serializer.is_valid():
        student = serializer.save()

        serializer2 = StudentSerializer(student)

        return Response(serializer2.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def student_put(request, name): 
    try:
        student = Student.objects.get(name=name)

    except Student.DoesNotExist:
        return Response({"errors": "Student tabylbady"}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = StudentCreateSerializer(student, data=request.data, partial=True)

    if serializer.is_valid():
        student = serializer.save()

        serializer2 = StudentSerializer(student)

        return Response(serializer2.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def student_delete(request,name):

    try:
        student = Student.objects.get(name=name)

    except Student.DoesNotExist:
        return Response({"errors": f"{name} degen Student  tabylbady"}, status=status.HTTP_404_NOT_FOUND)

    student.delete()

    return Response({"message": f"{name} degen student ochuruldu"}, status=status.HTTP_200_OK)