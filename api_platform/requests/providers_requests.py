from django.http import JsonResponse
from django.db import connections
from django.db import InternalError as errors, IntegrityError as errors, InterfaceError as errors, ProgrammingError as errors
import json

def show_providers(request):
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.callproc("PROVEEDORES_MOSTRAR")
        return JsonResponse({"msg": cursor.fetchall()}, status=200)
    except (errors) as e:
        print(e)
        return JsonResponse({"msg": None}, status=200)

def create_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses)
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("PROVEEDOR_AGREGAR", [responses.get("cod_prov"), responses.get("nombre"), responses.get("telefono"), responses.get("email"), responses.get("pais")])
            return JsonResponse({"status": "success", "msg": "Proveedor agregado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modify_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses)
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("PROVEEDOR_MODIFICAR", [responses.get("nombre"), responses.get("telefono"), responses.get("email"), responses.get("pais"), responses.get("cod_prov")])
            return JsonResponse({"status": "success", "msg": "Proveedor actualizado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses)
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("ELIMINAR_PROVEEDOR", [responses.get("cod_prov")])
            return JsonResponse({"status": "success", "msg": "Proveedor eliminado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_provider_from_item(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("PROVEEDOR_CAMBIAR_A_ITEM", [None, responses.get("id")])
            return JsonResponse({"status": "success", "msg": "Proveedor eliminado de item"}, status=200)
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
            print(responses.get("_email") if responses.get("_email") != None else "")
            print(responses.get("country") if responses.get("country") != None else "")
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("PROVEEDOR_COMPLETO_A_ITEM", [responses.get("item_id") if responses.get("item_id") != None else "", responses.get("prov_id") if responses.get("prov_id") != None else "", responses.get("p_nombre") if responses.get("p_nombre") != None else "", responses.get("numero_t") if responses.get("numero_t") != None else "", responses.get("_email") if responses.get("_email") != None else "", responses.get("country") if responses.get("country") != None else ""])
            mensaje = cursor.fetchone()[0]
            if mensaje == '':
                return JsonResponse({"status": "success", "msg": "Proveedor agregado a item"}, status=200)
            else:
                return JsonResponse({"status": "error", "msg": mensaje}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def change_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("PROVEEDOR_CAMBIAR_A_ITEM", [responses.get("prov_id") if responses.get("prov_id") != "QUITAR" else None, responses.get("item_id")])
            return JsonResponse({"status": "success", "msg": "Proveedor actualizado"}, status=200)
        except (errors) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def search_provider(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("prov_id"))
        try:
            cursor = connections["sigssmac_db"].cursor()
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