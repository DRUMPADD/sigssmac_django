from django.http import JsonResponse
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
        print(responses.get("prov_id"))
        print(responses.get("p_nombre"))
        print(responses.get("numero_t"))
        print(responses.get("email"))
        print(responses.get("country"))
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO proveedores (cod_prov, nombre, telefono, email, pais) values(%s, %s, %s, %s, %s)", [responses.get("prov_id"), responses.get("p_nombre"), responses.get("numero_t"), responses.get("email"), responses.get("country")])
            return JsonResponse({"status": "success", "msg": "Proveedor agregado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modify_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("prov_id"))
        print(responses.get("p_nombre"))
        print(responses.get("numero_t"))
        print(responses.get("email"))
        print(responses.get("country"))
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE proveedores SET nombre = %s, telefono = %s, email = %s, pais = %s where cod_prov = %s", [responses.get("p_nombre"), responses.get("numero_t"), responses.get("email"), responses.get("country"), responses.get("prov_id")])
            return JsonResponse({"status": "success", "msg": "Proveedor actualizado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("prov_id"))
        try:
            cursor = connection.cursor()
            cursor.callproc("ELIMINAR_PROVEEDOR", [responses.get("prov_id")])
            return JsonResponse({"status": "success", "msg": "Proveedor eliminado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def add_provider_to_item(request):
    if request.method == 'POST':
        mensaje = ""
        try:
            responses = json.loads(request.body.decode("utf-8"))
            print(responses)
            print(responses.get("item_id") if responses.get("item_id") != None else "")
            print(responses.get("prov_id") if responses.get("prov_id") != None else "")
            print(responses.get("p_nombre") if responses.get("p_nombre") != None else "")
            print(responses.get("numero_t") if responses.get("numero_t") != None else "")
            print(responses.get("email") if responses.get("email") != None else "")
            print(responses.get("country") if responses.get("country") != None else "")
            cursor = connection.cursor()
            cursor.callproc("PROVEEDOR_COMPLETO_A_ITEM", [responses.get("item_id") if responses.get("item_id") != None else "", responses.get("prov_id") if responses.get("prov_id") != None else "", responses.get("p_nombre") if responses.get("p_nombre") != None else "", responses.get("numero_t") if responses.get("numero_t") != None else "", responses.get("email") if responses.get("email") != None else "", responses.get("country") if responses.get("country") != None else ""])
            mensaje = cursor.fetchone()[0]
            if mensaje == '':
                return JsonResponse({"status": "success", "msg": "Proveedor agregado a item"}, status=200)
            else:
                return JsonResponse({"status": "success", "msg": mensaje}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def change_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE maquinas_equipos SET proveedor = %s where maq_eq_id = %s", [responses.get("prov_id") if responses.get("prov_id") != "QUITAR" else None, responses.get("item_id")])
            return JsonResponse({"status": "success", "msg": "Proveedor actualizado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def search_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("prov_id"))
        try:
            cursor = connection.cursor()
            cursor.callproc("BUSCAR_PROVEEDOR_EXISTENTE", [responses.get("prov_id")])
            resp = cursor.fetchall()
            print(resp)
            if resp:
                return JsonResponse({"msg": "EXISTE"}, status=200)
            else:
                return JsonResponse({"msg": ""}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)