from sqlite3 import ProgrammingError
from django.shortcuts import render
from django.db import connection, OperationalError, DatabaseError, InternalError
# Create your views here.
def general_view(request):
    context = {
        "title": "Principal",
    }
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM maquinas_equipos")
        context["items"] = cursor.fetchall()
        cursor2 = connection.cursor()
        cursor2.execute("SELECT * FROM frecuencia")
        context["frequence"] = cursor2.fetchall()
        cursor3 = connection.cursor()
        cursor3.execute("SELECT * FROM actividades")
        context["activities"] = cursor3.fetchall()
    except (OperationalError, DatabaseError, InternalError) as e:
        print(e)
    return render(request, "plataforma/general.html", context)

def activities_view(request):
    context = {
        "title": "Actividades",
    }
    return render(request, "plataforma/activities.html", context)

def items_view(request):
    context = {
        "title": "Listado de máquinas o equipo",
    }
    return render(request, "plataforma/items.html", context)

def item_view(request, id_item):
    context = {}
    print("ID:",id_item)
    if id_item != '':
        try:
            cursor = connection.cursor()
            cursor.callproc("CARACTERISTICAS_ITEM", [id_item])
            get_info = cursor.fetchall()
            context["caracteristicas"] = get_info
            if get_info:
                context["existe"] = True
                context["title"] = 'Item ' + id_item
        except (OperationalError, DatabaseError, ProgrammingError) as e:
            print(e)
        finally:
            cursor.close()
        return render(request, "plataforma/item.html", context)
    else:
        context["title"] = 'Item no encontrado'
        context["existe"] = False
        return render(request, "plataforma/item.html", context)

# def manteinment_1_view(request):
#     context = {
#         "title": "Mantenimiento preventivo",
#         "message": "Esta ventana es para mantenimiento preventivo"
#     }
#     return render(request, "manteinment1.html", context)

def manteinment_view(request):
    context = {
        "title": "Mantenimiento correctivo",
    }
    return render(request, "plataforma/manteinment.html", context)