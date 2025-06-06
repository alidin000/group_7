from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Student

# Create your views here.
def main_page(request):
    return HttpResponse("<h1>Hello</h1>")


def student_page(request): 
    students = Student.objects.all()
    context = {"students": students}
    return render(request,'student\main_page.html', context)

def student_by_id(request, name):
    try:
        student = get_object_or_404(Student, name = name)
        context = {"student": student}
    except Http404 as http:
        context = {"student": None}
    return render(request,'student\student.html', context)
