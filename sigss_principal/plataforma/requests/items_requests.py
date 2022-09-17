from django.http import JsonResponse
from django.db import connection
from django.db import InternalError, IntegrityError, InterfaceError, ProgrammingError
import json

def show_items(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM maquinas_equipos")
        items = cursor.fetchall()
        print(items)
        return JsonResponse({"msg": items}, status=200)
    except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
        print(e)
        return JsonResponse({"msg": None}, status=200)

def create_item(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("cod_item"))
        print(responses.get("name_item"))
        print(responses.get("quantity"))
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO maquinas_equipos (maq_eq_id, n_item, cantidad) values(%s, %s, %s)", (responses.get("cod_item"), responses.get("name_item"), responses.get("quantity")))
            return JsonResponse({"status": "success", "msg": "Item agregado"}, status=200)
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()

def modify_item(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("id_"))
        print(responses.get("new_name"))
        print(responses.get("new_stuck"))
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE maquinas_equipos set n_item = %s, cantidad = %s where maq_eq_id = %s", (responses.get("new_name"), responses.get("new_stuck"), responses.get("id_")))
            return JsonResponse({"status": "success", "msg": "Item actualizado"}, status=200)
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
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
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
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
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
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
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
        finally:
            cursor.close()