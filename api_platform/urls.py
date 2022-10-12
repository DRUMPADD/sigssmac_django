from django.urls import path
from api_platform.views import *

urlpatterns = [
    path("", index, name="generalMantAPI"),
    path("actividades", activities, name="activitiesAPI"),
    path("equipos", items, name="itemsAPI"),
    path("mantenimiento-correctivo", correc_manteinment, name="corMantAPI"),
    path("otros-registros", other_views, name="otherRegistersAPI"),
]