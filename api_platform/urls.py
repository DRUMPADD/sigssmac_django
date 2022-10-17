from django.urls import path
from api_platform.views import *
from api_platform.accidents import *
urlpatterns = [
    path("", index, name="generalMantAPI"),
    path("/actividades", activities, name="activitiesAPI"),
    path("/equipos", items, name="itemsAPI"),
    path("/mantenimiento-correctivo", correc_manteinment, name="corMantAPI"),
    path("/otros-registros", other_views, name="otherRegistersAPI"),

    # ?? Accidentabilidad
    path("/accidentabilidad", accidentability_view, name="accidentabilityAPI"),
    path("/datos_generales_obtenidos", data_every_month, name="datos_generales_obtenidos"),
    path("/registrar_accidente", register_accident, name="registrar_info"),
]