import json
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .models import Student
# Create your views here.
# HTTP  communication between browser and server/ api

# HTTP REQUEST -> ЗАПРОС
# METHOD
# URL 
# HEADER 
# BODY

# HTTP RESPONSE 
# STATUS CODE => 200 OK, 404 NOT FOUND, 500 SERVER ERROR 
# HEADER 
# BODY 

# HTTP RESPONSE -> ОТВЕТ

# methods 
# GET
# POST
# PUT
# DELETE

# URL: '/students/get_list/'
@csrf_exempt
def hello_json(request): 

    try:
        if request.method == 'POST':

            data = json.loads(request.body)

            return JsonResponse({"alyngan_data": data}, status=200)
    except json.JSONDecodeError as js:
        return JsonResponse({"error": f"Invalid json - {js} KATA" }, status = 500)
    
    # elif request.method == 'GET':
    return JsonResponse({"message": "Only post method allowed"})

@csrf_exempt
def get_students(request):
    students = Student.objects.all()

    st = [s for s in students]

    return HttpResponse(st)

@csrf_exempt
def get_students_post_man(request):
    try:
        if request.method == 'GET':
            data = Student.objects.all()
            # data = json.loads(request.body)
            data = [f"({s.name}, {s.email}, {s.age})" for s in data]
            print(data)
            return JsonResponse({"alyngan_data": data}, status=302)
    except json.JSONDecodeError as js:
        return JsonResponse({"error": f"Invalid json - {js} KATA" }, status = 500)
    
    # elif request.method == 'GET':
    return JsonResponse({"message": "Only GET method allowed"})
    
@csrf_exempt
def create_student(request):
    try:
        if request.method == 'POST':

            data = json.loads(request.body)


            # { 
            #     name: "name"
            #     email: "email"
            #     age: 'age'
            #     attendance  "attendance"
            # }

            def check_for_the_age(age: int) -> bool:
                if age < 18:
                    return False
                else:
                    return True

            try:
                if not check_for_the_age(data['age']):
                    raise ValueError("Sen univerge tapshyra albaisyn")
                
                jany_student = Student.objects.create(name=data['name'], age=data['age'], email=data['email'], attendance=data['attendance'])

            except Exception as e:
                return JsonResponse({"error":f"Student kirbei kaldy. Sebebi: {e}"}, status=500)


            result = {
                'message': 'Student jasaldy ✅',
                'student':data,
            }

            return JsonResponse(result, status=200)
    except json.JSONDecodeError as js:
        return JsonResponse({"error": f"Invalid json - {js} KATA" }, status = 500)
    
    # elif request.method == 'GET':
    return JsonResponse({"message": "Only POST, student kirgizuu uchun"})


@csrf_exempt
def find_student(request):
    
    if request.method != "GET":
        return JsonResponse({"error": "Only get method allowed"}, status=404)

    def find(name: str) -> Student:
        st = get_object_or_404(Student, name=name)
        
        return st
    try:
        data = json.loads(request.body.decode('utf-8'))

        # {
        #     "name": "name"
        # }

        name = data["name"]
        try:
            st = find(name)
        except Http404 as http:
            return JsonResponse({"error": f"Tabylbady {str(http)}"}, status=303)

        return JsonResponse({"message": f"student tabyldy: {(st.name, st.attendance, st.email, st.age)}"}, status=302)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)