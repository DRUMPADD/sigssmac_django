from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.db import InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError
import json

def showFrequences(request):
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM frecuencia")
        return JsonResponse({"msg": cursor.fetchall()}, status=200)
    except (InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError) as e:
        print(e)
        return JsonResponse({"msg": None}, status=200)

def createFrequence(request):
    if request.method == 'POST':
        answers = json.loads(request.body.decode("utf-8"))
        print(answers)
        try:
            cursor = connection.cursor()
            cursor.callproc("FRECUENCIA_AGREGAR", [answers.get("name")])
            return JsonResponse({"status": "success", "msg": "Frecuencia agregada"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def modifyFrequence(request):
    if request.method == 'POST':
        answers = json.loads(request.body.decode("utf-8"))
        print(answers)
        try:
            cursor = connection.cursor()
            cursor.callproc("FRECUENCIA_MODIFICAR", [answers.get("id"), answers.get("name")])
            return JsonResponse({"status": "success", "msg": "Frecuencia: "+ answers.get("id") +" actualizada"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)

def deleteFrequence(request):
    if request.method == 'POST':
        answers = json.loads(request.body.decode("utf-8"))
        print(answers)
        try:
            cursor = connection.cursor()
            cursor.callproc("FRECUENCIA_ELIMINAR", [answers.get("id")])
            return JsonResponse({"status": "success", "msg": "Frecuencia: "+ answers.get("id") +" eliminada"}, status=200)
        except (InternalError, IntegrityError, InterfaceError, ProgrammingError, DataError, OperationalError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Error en el sistema"}, status=200)