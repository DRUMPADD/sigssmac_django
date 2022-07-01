from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.db import connection
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.utils import *
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get("usuario")
        password = request.POST.get("contrasenia")

        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return HttpResponseRedirect("/tarco")
        else:
            msg = "<head><link rel='stylesheet' href='https://bootswatch.com/5/zephyr/bootstrap.min.css'></head><html><body class='container text-center'><h1 class='h1'>El usuario no existe</h1><br><br><a href='/inicio_sesion' class='btn btn-primary'>Regresar</a></body></html>"
            return HttpResponse(msg)

def inicio(request):
    return render(request, "login.html")

def cerrar(request):
    logout(request)
    return redirect("inicio_sesion")

def principal(request):
    return render(request, "index.html")

def enviar_mensaje(request):
    if request.method == 'POST':
        cursor = connection.cursor()
        nombre = request.POST.get("nombre")
        apellidos = str(request.POST.get("apellidos")).split(" ")
        email_ = request.POST.get("email")
        mensaje = request.POST.get("mensaje")
        if len(apellidos) == 1:
            cursor.callproc("CONTACTO", [email_, nombre, apellidos[0], "", mensaje])
            mensaje_email = "Nombre: " + str(nombre) +" " + apellidos[0] + "\n" + "Mensaje: " + mensaje + "\nContacto: " + email_
        else:
            cursor.callproc("CONTACTO", [email_, nombre, apellidos[0], apellidos[1], mensaje])
            mensaje_email = "Nombre: " + str(nombre) +" " + apellidos[0] + " " + apellidos[1] + "\n" + "Mensaje: " + mensaje + "\nContacto: " + email_

        send_mail(subject="Solicitud de cotización", message=mensaje_email, from_email=email_, recipient_list=["ventas.sigssmac@gmail.com", "sti1.sigssmac@outlook.com", "ventas.sigssmac@outlook.com"], fail_silently=False)
        return JsonResponse({"msg": "Su mensaje ha sido enviado"}, status=200)

def db_operational_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except OperationalError:
            return HttpResponse("Error en la base de datos")
    return inner_function

@login_required(login_url="inicio_sesion")
@db_operational_handler
def index(request):
    context = {
        "title": "TARCO"
    }
    return render(request, "tarco.html", context)

@db_operational_handler
def informacion(request):
    if request.method == 'GET':
        mensaje = ""
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * from items")
            mensaje = cursor.fetchall()
            return JsonResponse({"status": "success", "info": mensaje}, status=200)
        except (InternalError, DatabaseError, IntegrityError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "info": "Hubo un error en el sistema"}, status=200)

def enviar_item(request):
    if request.method == 'POST':
        post_d = json.loads(request.body.decode("utf-8"))

        datos_item = (post_d.get("id"), post_d.get("nombre"), post_d.get("car"), post_d.get("ubi"), post_d.get("frec"), post_d.get("fec_ins"), post_d.get("conds"), post_d.get("fec_col"), post_d.get("fec_reem"), post_d.get("cond"))
        try:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO items (item, elemento, caracteristicas, ubicacion, frec_ins, fech_ins, condiciones, fech_col, fech_reem, condicion) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", datos_item)
            return JsonResponse({"status": "success", "msg": "Datos enviados"}, status=200)
        except (InternalError, DatabaseError, IntegrityError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Hubo un error en el sistema"}, status=200)

@db_operational_handler
def modificar_item(request):
    if request.method == 'POST':
        post_d = json.loads(request.body.decode("utf-8"))

        datos_item = (post_d.get("nombre"), post_d.get("car"), post_d.get("ubi"), post_d.get("frec"), post_d.get("fec_ins"), post_d.get("conds"), post_d.get("fec_col"), post_d.get("fec_reem"), post_d.get("cond"), post_d.get("id"))
        try:
            cursor = connection.cursor()
            cursor.execute("UPDATE items set elemento = %s, caracteristicas = %s, ubicacion = %s, frec_ins = %s, fech_ins = %s, condiciones = %s, fech_col = %s, fech_reem = %s, condicion = %s where item = %s", datos_item)
            return JsonResponse({"status": "success", "msg": "Item modificado"}, status=200)
        except (InternalError, DatabaseError, IntegrityError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Hubo un error en el sistema"}, status=200)

@db_operational_handler
def eliminar_item(request):
    if request.method == 'POST':
        post_data = json.loads(request.body.decode("utf-8"))
        id_item = str(post_data.get("id"))
        print(id_item)

        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM items where item = %s", [id_item])

            return JsonResponse({"status": "success", "msg": "Item eliminado"}, status=200)
        except (InternalError, DatabaseError, IntegrityError, ProgrammingError) as e:
            print(e)
            return JsonResponse({"status": "error", "msg": "Hubo un error en el sistema"}, status=200)