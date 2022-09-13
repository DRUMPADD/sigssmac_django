from django.http import JsonResponse
from django.db import connection
from django.db import InternalError as errors, IntegrityError as errors, InterfaceError as errors, ProgrammingError as errors
import json

def create_item(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor2 = connection.cursor()
            cursor.execute("")
            cursor2.execute("")
            return JsonResponse({"status": "success", "msg": "Item agregado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()
            cursor2.close()

def modify_item(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
            return JsonResponse({"status": "success", "msg": "Item actualizado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()

def delete_item(request):
    if request.method == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute("")
            return JsonResponse({"status": "success", "msg": "Item eliminado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()

def search_item(request):
    if request.methods == 'GET':
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * from items where codigo = %s", [request.POST.get("codigo")])
            return JsonResponse({"status": "success", "msg": cursor.fetchall()}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()

def caract_item(request):
    if request.methods == 'POST':
        try:
            cursor = connection.cursor()
            cursor.execute()
            return JsonResponse({"status": "success", "msg": "Características agregadas a item"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()