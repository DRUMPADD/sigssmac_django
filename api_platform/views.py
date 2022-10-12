from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Mantenimiento preventivo"
    }
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

def correc_manteinment(request):
    context = {
        "title": "Mantenimiento correctivo"
    }
    return render(request, "api_energy/manteinment.html", context)

def other_views(request):
    context = {
        "title": "Otros registros"
    }
    return render(request, "api_energy/other.html", context)