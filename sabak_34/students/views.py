from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from students.models import Student
from students.serializers import StudentSerializer

# Create your views here.
@crsf_
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()  # select * from Students;
    serializer = StudentSerializer(students, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_student(request):
    student = Student.objects.get(id=1)  # select * from Students;
    serializer = StudentSerializer(student)

    return Response(serializer.data)
