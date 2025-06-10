import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

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
        return JsonResponse({"error": f"Invalid json - {js}" }, status = 400)
    
    # elif request.method == 'GET':
    return JsonResponse({"message": "Only post method allowed"})
    
