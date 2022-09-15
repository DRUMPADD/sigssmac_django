from sqlite3 import ProgrammingError
from django.shortcuts import render
from django.db import connection, OperationalError, DatabaseError
# Create your views here.
def general_view(request):
    context = {
        "title": "Principal",
    }
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
    try:
        cursor = connection.cursor()
        cursor.callproc("MOSTRAR_CARACTERISTICAS_ITEM", [id_item])
        context["caracteristicas"] = cursor.fetchall()
    except (OperationalError, DatabaseError, ProgrammingError) as e:
        print(e)
    finally:
        cursor.close()
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