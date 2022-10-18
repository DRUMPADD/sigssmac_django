from django.urls import path
from mcgreen_platform.views import *
from mcgreen_platform.accidents import *
urlpatterns = [
    path("", index, name="generalMantMCGREEN"),
    path("actividades", activities, name="activitiesMCGREEN"),
    path("equipos", items, name="itemsMCGREEN"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantMCGREEN"),
    path("otros-registros", other_view, name="otherRegistersMCGREEN"),

    # ?? Accidentabilidad
    path("accidentabilidad", accidentability_view, name="accidentabilityMCGREEN"),
]