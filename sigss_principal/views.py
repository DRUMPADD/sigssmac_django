from django.shortcuts import render, redirect
from django.core.mail import send_mail

# Create your views here.
def principal(request):
    return render(request, "index.html")

def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST.get("nombre") + request.POST.get("apellidos")
        email_ = request.POST.get("email")
        mensaje = "Nombre: " + str(nombre) + "\n" + "Mensaje: " + request.POST.get("mensaje") + "\nContacto: " + email_
        send_mail(subject="Solicitud de cotización", message=mensaje, from_email=email_, recipient_list=["ventas.sigssmac@gmail.com", "sti1.sigssmac@outlook.com", "ventas.sigssmac@outlook.com"], fail_silently=False)
        return redirect("inicio")