from django.http import JsonResponse
from django.db import connection
from django.db import InternalError, IntegrityError, InterfaceError, ProgrammingError
import json


def show_general_mant(request):
    try:
        cursor = connection.cursor()
        cursor.callproc("MOSTRAR_MANTENIMIENTO_PREVENTIVO")
        get_info = cursor.fetchall()
        return JsonResponse({"msg": get_info}, status=200)
    except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
        print(e)
        return JsonResponse({"msg": "Error en el sistema"}, status=200)
    except ValueError as e:
        return JsonResponse({"msg": "Error en el sistema"}, status=200)
    finally:
        cursor.close()


def create_general(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.callproc("REGISTRAR_MANTENIMIENTO_PREVENTIVO", [responses.get("item_id"), responses.get("frec_"), responses.get("create_date"), responses.get("act_"), responses.get("date_next")])
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo agregado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modify_general(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        print(responses.get("item_id"))
        print(responses.get("frec_"))
        print(responses.get("create_date"))
        print(responses.get("act_"))
        print(responses.get("date_next"))
        print(responses.get("prev_cod"))
        try:
            cursor = connection.cursor()
            cursor.callproc("ACTUALIZAR_MANTENIMIENTO_PREVENTIVO", [responses.get("item_id"), responses.get("frec_"), responses.get("create_date"), responses.get("act_"), responses.get("date_next"), responses.get("prev_cod")])
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo actualizado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_general(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM mantenimiento_prev where id_prev = %s", [responses.get("prev_id")])
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo eliminado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
