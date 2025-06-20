from rest_framework import serializers
from .models import Course, Student


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student

        fields = "__all__"

class StudentCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class CourseCreatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    def validate_title(self, title):

        list_of_titles = set(["Python", "C++", "Java"])

        if title in list_of_titles:
            return title
        
        raise serializers.ValidationError(f"Course should be one of these: {list_of_titles}")

    

class CourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course

        fields = "__all__"
