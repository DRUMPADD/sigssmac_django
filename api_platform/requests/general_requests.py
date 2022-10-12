from django.http import JsonResponse, HttpResponse
from django.db import connections
from django.db import InternalError, IntegrityError, InterfaceError, ProgrammingError
import json


def show_general_mant(request):
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.callproc("MOSTRAR_MANTENIMIENTO_PREVENTIVO")
        get_info = cursor.fetchall()
        return JsonResponse({"msg": get_info}, status=200)
    except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
        print(e)
        return JsonResponse({"msg": "Error en el sistema"}, status=200)
    except ValueError as e:
        return HttpResponse("<h1>Nada</h1>")
    finally:
        cursor.close()


def create_general(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.execute("INSERT INTO mantenimiento_prev (maq_eq_id_fk, frec_id_fk, fec_creacion, act_id_fk, fecha_prox) values(%s, %s, %s, %s, %s)", [responses.get("item_id"), responses.get("frec_"), responses.get("create_date"), responses.get("act_"), responses.get("date_next")])
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
            cursor = connections["api_energy_db"].cursor()
            cursor.execute("UPDATE mantenimiento_prev SET maq_eq_id_fk = %s, frec_id_fk = %s, fec_creacion = %s, act_id_fk = %s, fecha_prox = %s where id_prev = %s", [responses.get("item_id"), responses.get("frec_"), responses.get("create_date"), responses.get("act_"), responses.get("date_next"), responses.get("prev_cod")])
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo actualizado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_general(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.execute("DELETE FROM mantenimiento_prev where id_prev = %s", [responses.get("prev_id")])
            return JsonResponse({"status": "success", "msg": "Mantenimiento preventivo eliminado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
