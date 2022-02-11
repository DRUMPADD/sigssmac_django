from django.shortcuts import render
from django.core.mail import send_mail
from django.db import connection
from django.http import JsonResponse

# Create your views here.
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