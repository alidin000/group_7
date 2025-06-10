from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from students.models import Student

from .forms import StudentForm
# Create your views here.

def temp_func(request):
    if request.method == 'GET':
        return HttpResponse("Bul <bold>GET</bold> method")
    elif request.method == 'POST':
        return HttpResponse("Bul <bold>POST</bold> method")
    else:
        print("do nothing")
    # return render(request, "")

# GET -> алуу 
# POST -> киргизуу, база данныхка 
def get_students(request):
    students = Student.objects.all()
    context = {"students": students}
    return render(request,'students\main_page.html', context)

def first_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_students')
    else:
        form = StudentForm()
    context = {"forms": form}
    return render(request,'students/base.html', context)


def edit_student(request, id):

    student = get_object_or_404(Student, id = id)

    form = StudentForm(request.POST or None, instance=student)
    print(student)
    if form.is_valid():
        form.save()
        return redirect("get_students")
    
    context = {"forms": form}
    return render(request,'students/base.html', context)
