from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "title": "Mantenimiento preventivo"
    }
    return render(request, "tarco/index.html", context)

def activities(request):
    context = {
        "title": "Actividades"
    }
    return render(request, "tarco/activities.html", context)

def items(request):
    context = {
        "title": "Equipos"
    }
    return render(request, "tarco/items.html", context)

def correc_manteinment(request):
    context = {
        "title": "Mantenimiento correctivo"
    }
    return render(request, "tarco/manteinment.html", context)

def other_views(request):
    context = {
        "title": "Otros registros"
    }
    return render(request, "tarco/other.html", context)