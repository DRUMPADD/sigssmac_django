from django.urls import path
from tarco_platform.views import *
from tarco_platform.accidents import *
urlpatterns = [
    path("", index, name="generalMantTARCO"),
    path("actividades", activities, name="activitiesTARCO"),
    path("equipos", items, name="itemsTARCO"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantTARCO"),
    path("otros-registros", other_views, name="otherRegistersTARCO"),


    # ?? Accidentabilidad
    path("accidentabilidad", accidentability_view, name="accidentabilityTARCO"),
]