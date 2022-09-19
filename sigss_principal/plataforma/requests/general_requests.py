from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.db import InternalError, IntegrityError, InterfaceError, ProgrammingError
import json


def show_general_mant(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.callproc("MOSTRAR_MANTENIMIENTO_PREVENTIVO")
            get_info = cursor.fetchall()
            print(get_info)
            general = get_info if get_info != [] else ""
            return JsonResponse({"msg": general}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError, ValueError) as e:
            print(e)
            return HttpResponse({"msg": "Envió nada"})


def create_general(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo agregado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modify_general(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo actualizado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_general(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo eliminado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
