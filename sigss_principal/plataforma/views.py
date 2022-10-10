from django.shortcuts import render, HttpResponse
from django.db import connections, OperationalError, DatabaseError, InternalError, DataError, IntegrityError, InterfaceError, ProgrammingError, NotSupportedError, Error
from django.template.exceptions import TemplateSyntaxError, TemplateDoesNotExist
# Create your views here.
def general_view(request):
    try:
        context = {
            "title": "Principal",
        }
        cursor = connections["sigssmac_db"].cursor()
        cursor.execute("SELECT * FROM maquinas_equipos")
        context["items"] = cursor.fetchall()
        cursor2 = connections["sigssmac_db"].cursor()
        cursor2.execute("SELECT * FROM frecuencia")
        context["frequence"] = cursor2.fetchall()
        cursor3 = connections["sigssmac_db"].cursor()
        cursor3.execute("SELECT * FROM actividades")
        context["activities"] = cursor3.fetchall()
        return render(request, "plataforma/general.html", context)
    except (OperationalError, DatabaseError, InternalError, DataError, IntegrityError, InterfaceError, ProgrammingError, NotSupportedError, Error) as e:
        print(e)
        return render(request, "plataforma/template_error.html")
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def activities_view(request):
    try:
        context = {
            "title": "Actividades",
        }
        return render(request, "plataforma/activities.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def items_view(request):
    try:
        context = {
            "title": "Listado de máquinas o equipo",
        }
        return render(request, "plataforma/items_new.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def item_view(request, id_item):
    context = {
        "item": id_item
    }
    print("ID:",id_item)
    try:
        cursor = connections["sigssmac_db"].cursor()
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
        cursor = connections["sigssmac_db"].cursor()
        cursor.execute("SELECT * FROM estado_plat")
        get_info = cursor.fetchall()
        context["states"] = get_info
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        cursor2 = connections["sigssmac_db"].cursor()
        cursor2.callproc("MOSTRAR_PROVEEDOR_EN_ITEM", [id_item])
        get_pro = cursor2.fetchall()
        context["existe_prov"] = True if get_pro else False
        context["provider"] = get_pro
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor2.close()
    try:
        cursor = connections["sigssmac_db"].cursor()
        cursor.execute("SELECT * FROM proveedores")
        get_pro = cursor.fetchall()
        context["providers"] = get_pro
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        return render(request, "plataforma/item.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def manteinment_view(request):
    context = {
        "title": "Mantenimiento correctivo",
    }
    try:
        cursor = connections["sigssmac_db"].cursor()
        cursor2 = connections["sigssmac_db"].cursor()
        cursor3 = connections["sigssmac_db"].cursor()
        cursor.execute("SELECT * FROM maquinas_equipos")
        cursor2.execute("SELECT * FROM modos_fallo")
        cursor3.execute("SELECT * FROM novedad")
        context["items"] = cursor.fetchall()
        context["fails"] = cursor2.fetchall()
        context["novedad"] = cursor3.fetchall()
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
        return HttpResponse("<h1>Ocurrió un error</h1>")
    finally:
        cursor.close()
        cursor2.close()
        cursor3.close()
    try:
        return render(request, "plataforma/manteinment.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def other_view(request):
    try:
        context = {
            "title": "Otros movimientos"
        }
        return render(request, "plataforma/others.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")