from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.db import InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError
import json


def show_activities(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM actividades")
        get_info = cursor.fetchall()
        activities = get_info if get_info != [] else "" 
        return JsonResponse({"msg": activities}, status=200)
    except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
        print(e)
        return JsonResponse({"status": "error","msg": []}, status=200)

def create_activity(request):
    if request.method == 'POST':
        try:
            responses = json.loads(request.body.decode("utf-8"))
            print(responses.get('cod_act'))
            print(responses.get('name_act'))
            print(responses.get('desc'))

            cursor = connection.cursor()
            cursor.execute("INSERT INTO actividades (codigo, n_act, descripcion) values(%s, %s, %s)", (responses.get('cod_act'), responses.get('name_act'), responses.get('desc')))
            return JsonResponse({"status": "success","msg": "Datos agregados con éxito"}, status=200)
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
            print(e)
            return JsonResponse({"status": "error","msg": "Error en el sistema"}, status=200)

def modify_activity(request):
    if request.method == 'POST':
        responses = json.loads(request.body.decode("utf-8"))

        print(responses.get("cod_act"))
        print(responses.get("newName"))
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE actividades SET n_act = %s where codigo = %s", (responses.get("newName"), responses.get("cod_act")))
            return JsonResponse({"status": "success", "msg": "Item "+ responses.get("cod_act")+" modificado"}, status=200)
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
            print(e)
            return JsonResponse({"status": "error","msg": "Error en el sistema"}, status=200)

def search_activity(request):
    if request.method == 'POST':
        response = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.callproc("BUSCAR_ACTIVIDAD_EN_MANTENIMIENTO", [response.get("id_act")])
            encontrado = cursor.fetchall()
            print(encontrado)
            if encontrado:
                return JsonResponse({"msg": "Encontrado"}, status=200)
            else:
                return JsonResponse({"msg": "No encontrado"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError) as e:
            print(e)
            return JsonResponse({"msg": "Error en el sistema"}, status=200)

def delete_activity(request):
    if request.method == 'POST':
        response = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM actividades where codigo = %s", [response.get("id_act")])
            return JsonResponse({"status": "success", "msg": "Actividad eliminada"}, status=200)
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def delete_activity_with_mant(request):
    if request.method == 'POST':
        response = json.loads(request.body.decode("utf-8"))
        try:
            cursor = connection.cursor()
            cursor.execute("ELIMINAR_ACTIVIDAD_CON_MANTENIMIENTO", [response.get("id_act")])
            return JsonResponse({"status": "success", "msg": "Actividad eliminada por completo"}, status=200)
        except (ProgrammingError, InternalError, InterfaceError, IntegrityError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)
