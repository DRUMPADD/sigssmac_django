from django.http import JsonResponse
from django.db import connections
from django.db import DatabaseError, IntegrityError, NotSupportedError, InterfaceError, OperationalError, ProgrammingError
import json
def register_accident(request):
    if request.method == 'POST':
        res = json.loads(request.body.decode('utf-8'))
        mensaje = ""
        print(res)
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("ACCIDENTABILIDAD", [int(res["c_personal"][0]), int(res["h_trabajo"][0]), int(res["jornada"][0]), int(res["c_personal"][1]), int(res["h_trabajo"][1]), int(res["jornada"][1]), res["mes"], res["anio"], int(res["acci_c_baja"][0]), int(res["acci_c_baja"][1]), int(res["dias_inc"][0]), int(res["dias_inc"][1])])
            return JsonResponse({"status": "success", "res": "Registro realizado"}, status=200)
        except (DatabaseError, IntegrityError, NotSupportedError, InterfaceError, OperationalError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "res": "Ocurrió un error en el sistema"}, status=200)