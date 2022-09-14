from django.shortcuts import render

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