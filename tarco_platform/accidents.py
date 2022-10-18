from django.http import JsonResponse
from django.db import connections
from django.db import DatabaseError, IntegrityError, NotSupportedError, InterfaceError, OperationalError, ProgrammingError
import json
def register_accident(request):
    if request.method == 'POST':
        res = json.loads(request.body.decode('utf-8'))
        print(res)
        try:
            cursor = connections["tarco_db"].cursor()
            cursor.callproc("ACCIDENTABILIDAD", [res["c_personal"][0], res["h_trabajo"][0], res["jornada"][0], res["c_personal"][1], res["h_trabajo"][1], res["jornada"][1], res["mes"], res["anio"], res["acci_c_baja"][0], res["acci_c_baja"][1], res["dias_inc"][0], res["dias_inc"][1]])
            return JsonResponse({"status": "success", "res": "Registro realizado"}, status=200)
        except (DatabaseError, IntegrityError, NotSupportedError, InterfaceError, OperationalError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "res": "Ocurrió un error en el sistema"}, status=200)