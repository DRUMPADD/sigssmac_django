from django.shortcuts import render
from django.template import TemplateDoesNotExist, TemplateSyntaxError
from django.db import connections
from django.db import OperationalError, DatabaseError, ProgrammingError
# Create your views here.
def index(request):
    context = {
        "title": "Mantenimiento preventivo"
    }
    return render(request, "mcgreen/index.html", context)

def activities(request):
    context = {
        "title": "Actividades"
    }
    return render(request, "mcgreen/activities.html", context)

def items(request):
    context = {
        "title": "Equipos"
    }
    return render(request, "mcgreen/items.html", context)

def item_view(request, id_item):
    context = {
        "item": id_item
    }
    print("ID:",id_item)
    try:
        cursor = connections["mcgreen_db"].cursor()
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
        cursor = connections["mcgreen_db"].cursor()
        cursor.execute("SELECT * FROM estado_plat")
        get_info = cursor.fetchall()
        context["states"] = get_info
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        cursor2 = connections["mcgreen_db"].cursor()
        cursor2.callproc("MOSTRAR_PROVEEDOR_EN_ITEM", [id_item])
        get_pro = cursor2.fetchall()
        context["existe_prov"] = True if get_pro else False
        context["provider"] = get_pro
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor2.close()
    try:
        cursor = connections["mcgreen_db"].cursor()
        cursor.execute("SELECT * FROM proveedores")
        get_pro = cursor.fetchall()
        context["providers"] = get_pro
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
    try:
        return render(request, "mcgreen/item.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")

def correc_manteinment(request):
    context = {
        "title": "Mantenimiento correctivo"
    }
    return render(request, "mcgreen/manteinment.html", context)

def other_view(request):
    try:
        context = {
            "title": "Otros movimientos"
        }
        return render(request, "mcgreen/other.html", context)
    except (TemplateDoesNotExist, TemplateSyntaxError) as er:
        print("Error en template:",er)
        return render(request, "plataforma/template_error.html")