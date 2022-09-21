from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.db import InternalError as errors, IntegrityError as errors, InterfaceError as errors, ProgrammingError as errors
import json

def show_providers(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM proveedores")
        return JsonResponse({"msg": cursor.fetchall()}, status=200)
    except (errors) as e:
        print(e)
        return JsonResponse({"msg": None}, status=200)

def create_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO proveedores (cod_prov, nombre, telefono, email, pais) values(%s, %s, %s, %s, %s)", [responses.get("cod_prov"), responses.get("nombre"), responses.get("telefono"), responses.get("email"), responses.get("pais")])
            return JsonResponse({"status": "success", "msg": "Proveedor agregado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modify_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE proveedores SET nombre = %s, telefono = %s, email = %s, pais = %s where cod_prov = %s", [responses.get("nombre"), responses.get("telefono"), responses.get("email"), responses.get("pais"), responses.get("cod_prov")])
            return JsonResponse({"status": "success", "msg": "Proveedor actualizado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.callproc("ELIMINAR_PROVEEDOR", [responses.get("cod_prov")])
            return JsonResponse({"status": "success", "msg": "Proveedor eliminado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
