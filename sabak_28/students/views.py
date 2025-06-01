from django.shortcuts import render

# Create your views here.

def base_html(request):
    return render(request, "students/base.html")


def head_html(request):
    return render(request,"students/head.html")