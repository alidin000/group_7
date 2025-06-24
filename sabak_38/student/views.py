from django.shortcuts import get_object_or_404, render


from rest_framework.decorators import api_view

from rest_framework.response import Response
from rest_framework import status

from student.models import Course, Student
from student.serializers import CourseCreatorSerializer, CourseSerializer, StudentCreatorSerializer, StudentSerializer

# class based views
from rest_framework.generics import ListAPIView, CreateAPIView, ListCreateAPIView
from rest_framework.viewsets import ViewSet

# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
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

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import  IsAdminUser, IsAuthenticated

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser, IsAuthenticated])
def student_delete(request, name):

    method = request.method

    if method == 'DELETE':
        try:
            student = Student.objects.get(name = name)
            student.delete()
            return Response({"message": f"{name} was deleted successfully"}, status=status.HTTP_200_OK)
        except Exception:
            return Response({"message": f"Student not found"}, status=status.HTTP_404_NOT_FOUND)
       
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


# class based views 
# "GET" -> method
class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseListView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


# POST -> method
class StudentCreateView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentCreatorSerializer


class CourseCreateView(CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseCreatorSerializer


# POST GET 
class CourseCreatListView(ListCreateAPIView):
    # default permission = > AllowAny
    queryset = Course.objects.all()
    permission_classes = [IsAdminUser]
    
    def get_serializer_class(self):
        get_s = CourseSerializer
        post_s = CourseCreatorSerializer

        if self.request.method == 'GET':
            return get_s
        
        elif self.request.method == 'POST':
            return post_s
        

class StudentCreatListView(ListCreateAPIView):
    queryset = Student.objects.all()
    
    def get_serializer_class(self):
        get_s = StudentSerializer
        post_s = StudentCreatorSerializer

        if self.request.method == 'GET':
            return get_s
        
        elif self.request.method == 'POST':
            return post_s
        



# viewset
class CourseViewSet(ViewSet):
    
    def list(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Course.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = CourseSerializer(user)
        return Response(serializer.data)
    
    def create(self, request):
        
        create_serializer = CourseCreatorSerializer(data=request.data)

        if create_serializer.is_valid():
            course = create_serializer.save()

            serializer = CourseSerializer(course)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response({"error": create_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
