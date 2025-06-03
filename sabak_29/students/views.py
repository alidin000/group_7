from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def main(request):
    return HttpResponse("<h1>Hello world</h1>")

context = {'first_name': 'Kadyr', 'last_name': 'Kadyrbekov', 'group': 'python 7'}
context_2 = {"info1": {'first_name': 'Kadyr', 'last_name': 'Kadyrbekov', 'group': 'python 7'}, 'info2': {'first_name': 'Kadyr2', 'last_name': 'Kadyrbekov2', 'group': 'python 8'}}

context_3 = {'users' : 
                [
                    {'first_name': 'Kadyr', 'last_name': 'Kadyrbekov', 'group': 'python 7'}, 
                    {'first_name': 'Kadyr2', 'last_name': 'Kadyrbekov2', 'group': 'python 8'}
                ]
            }

context_4 = {}

def base(request): 
    return render(request, 'students/base.html', context_3)

def child_base(request):
    return render(request, 'students/child_base.html', context_3)