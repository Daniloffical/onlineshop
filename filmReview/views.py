from django.shortcuts import render
from .models import Film
from django.core.mail import send_mail, BadHeaderError
# Create your views here.


def show_films(request):
    films = Film.objects.all()
    return render(request, 'index.html', context = {'films':films})

def get_reply(request):
    name = request.POST.get("name")
    reply = request.POST.get("reply")
    message = f"Клієнт {name} залишив свій відгук:\n{reply}"
    send_mail('', message, 'settings.EMAIL_HOST_USER', ['userp9658@gmail.com'])
    films = Film.objects.all()
    return render(request, 'index.html', context = {'films':films})