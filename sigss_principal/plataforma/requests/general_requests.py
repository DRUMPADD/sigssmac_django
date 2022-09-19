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
            print("Yo habia ponido mi informacion aqui:",get_info)
            general = get_info if get_info else []
            try:
                print(general)
                return JsonResponse({"msg": general}, status=200)
            except ValueError as e:
                print(e)
                print("Nada dentro del try")
                return HttpResponse("<h1>Nada</h1>")
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            print("Nada dentro de except")
            return JsonResponse({"msg": "Error en el sistema"}, status=200)
        except ValueError as e:
            print(e)
            print("Nada dentro de except valueerror")
            return HttpResponse("<h1>Nada</h1>")


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
