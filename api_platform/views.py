from django.http import JsonResponse
from django.shortcuts import render
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.db import connections
from django.db import DatabaseError, IntegrityError, NotSupportedError, InterfaceError, OperationalError, ProgrammingError, InternalError
# Create your views here.
def index(request):
    context = {
        "title": "Mantenimiento preventivo"
    }
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.execute("SELECT * FROM maquinas_equipos")
        context["items"] = cursor.fetchall()
        cursor2 = connections["api_energy_db"].cursor()
        cursor2.execute("SELECT * FROM frecuencia")
        context["frequence"] = cursor2.fetchall()
        cursor3 = connections["api_energy_db"].cursor()
        cursor3.execute("SELECT * FROM actividades")
        context["activities"] = cursor3.fetchall()
    except (OperationalError, DatabaseError, InternalError) as e:
        print(e)
    return render(request, "api_energy/index.html", context)

def activities(request):
    context = {
        "title": "Actividades"
    }
    return render(request, "api_energy/activities.html", context)

def items(request):
    context = {
        "title": "Equipos"
    }
    return render(request, "api_energy/items.html", context)

def item_view(request, id_item):
    context = {
        "item": id_item
    }
    print("ID:",id_item)
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.callproc("CARACTERISTICAS_ITEM", [id_item])
        get_info = cursor.fetchall()
        ar = []
        for car in get_info:
            if car[1] == id_item:
                ar.append(car)
        context["caracteristicas"] = ar
        context["title"] = 'Item ' + id_item
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.execute("SELECT * FROM estado_plat")
        get_info = cursor.fetchall()
        context["states"] = get_info
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        cursor2 = connections["api_energy_db"].cursor()
        cursor2.callproc("MOSTRAR_PROVEEDOR_EN_ITEM", [id_item])
        get_pro = cursor2.fetchall()
        context["existe_prov"] = True if get_pro else False
        context["provider"] = get_pro
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor2.close()
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.execute("SELECT * FROM proveedores")
        get_pro = cursor.fetchall()
        context["providers"] = get_pro
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        return render(request, "api_energy/item.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def correc_manteinment(request):
    context = {
        "title": "Mantenimiento correctivo"
    }
    return render(request, "api_energy/manteinment.html", context)

def other_views(request):
    try:
        context = {
            "title": "Otros movimientos"
        }
        return render(request, "api_energy/other.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def accidentability_view(request):
    try:
        context = {
            "title": "Accidentabilidad"
        }
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.execute("select * from app_personal_propio")
            context["personal_propio"] = cursor.fetchall()
        except (OperationalError, InterfaceError, ProgrammingError) as e:
            print(e)
            return render(request, "plataforma/template_error.html", {
                "mensaje": "Contacte con el servicio de sistemas"
            })
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.execute("select * from app_personal_con")
            context["personal_contratado"] = cursor.fetchall()
        except (OperationalError, InterfaceError, ProgrammingError) as e:
            print(e)
            return render(request, "plataforma/template_error.html", {
                "mensaje": "Contacte con el servicio de sistemas"
            })
        try:
            cursor = connections["api_energy_db"].cursor()
            cursor.callproc("DETALLES_ACCIDENTABILIDAD")
            estadisticas = cursor.fetchall()
            context["detalles_acci"] = estadisticas
            cont_total_acc = 0
            cont_emp = 0
            for est in estadisticas:
                cont_total_acc = cont_total_acc + est[4]
                cont_emp = cont_emp + est[1]
            context["total_est"] = cont_total_acc
            context["total_emp"] = cont_emp
        except (DatabaseError, IntegrityError, NotSupportedError, InterfaceError, OperationalError, ProgrammingError) as e:
            print(e)
            return render(request, "plataforma/template_error.html", {
                "mensaje": "Contacte con el servicio de sistemas"
            })
        return render(request, "api_energy/accidents.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print(er)
        return render(request, "plataforma/template_error.html")

def data_every_month(request):
    mensaje = ""
    try:
        cursor = connections["api_energy_db"].cursor()
        cursor.callproc("DETALLES_ACCIDENTABILIDAD")
        mensaje = cursor.fetchall()
        print(mensaje)
        for con in mensaje:
            print(con)
        return JsonResponse({"respuesta": mensaje}, status=200) 
    except (OperationalError, InternalError, ProgrammingError) as e:
        print(e)
        return JsonResponse({"respuesta": "Error en el sistema"}, status=200)