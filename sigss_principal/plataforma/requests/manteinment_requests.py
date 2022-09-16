from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.db import InternalError as errors, IntegrityError as errors, InterfaceError as errors, ProgrammingError as errors
import json

def create_manteinment(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modify_manteinment(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_manteinment(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)