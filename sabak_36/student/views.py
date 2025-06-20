from django.shortcuts import render


from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

from student.models import Course, Student
from student.serializers import CourseCreatorSerializer, CourseSerializer, StudentCreatorSerializer, StudentSerializer
# Create your views here.

@api_view(['GET', 'POST'])
def student(request):

    method = request.method

    if method == 'GET':
        students = Student.objects.all()

        stud_serializer = StudentSerializer(students, many=True)

        return Response(stud_serializer.data, status=status.HTTP_200_OK)

    elif method == 'POST':
        create_serializer = StudentCreatorSerializer(data=request.data)

        if create_serializer.is_valid():
            student = create_serializer.save()

            serializer = StudentSerializer(student)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": create_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
            
    return Response({"message": f"Hello this is {method} method type"}, status=status.HTTP_200_OK)



@api_view(['GET', 'POST'])
def course(request):

    method = request.method

    if method == 'GET':
        courses = Course.objects.all()

        course_serializer = CourseSerializer(courses, many=True)

        return Response(course_serializer.data, status=status.HTTP_200_OK)

    elif method == 'POST':
        create_serializer = CourseCreatorSerializer(data=request.data)

        print("working")
        if create_serializer.is_valid():
            course = create_serializer.save()

            serializer = CourseSerializer(course)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": f"not valid course title"}, status=status.HTTP_400_BAD_REQUEST)
            
    return Response({"message": f"Hello this is {method} method type"}, status=status.HTTP_200_OK)