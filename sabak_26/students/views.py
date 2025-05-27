from django.shortcuts import render,HttpResponse
from .models import Student
# Create your views here.

def list_students(request):
    students = Student.objects.all() # select * from students
    st = Student.objects.filter(aty="Usser")
    print(list(students.values()))
    l = []
    for stud in list(students):
        print(stud)
        l.append(stud.__str__())

    
    student2 = Student.objects.filter(aty="Manas")
    student2.delete()
    Student.objects.create(aty="aty",fam='dfd', email='email@gmail.com',tuulgan_kunu='2000-02-02')
    return HttpResponse(f"{" ".join(st[0].__str__())}")