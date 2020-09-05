from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random
import os
import datetime

def time(request):
    return HttpResponse("Hi there ,,, time now is :"+ str(datetime.datetime.now()))


def passwd(request):
    chars = list('abecdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('splchar'):
        chars.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        chars.extend(list('1234567890'))

    length = int(request.GET.get('length',12))
    thepasswd = ''
    for x in range(length):
        thepasswd += random.choice(chars)

    return render(request, 'gen/passwd.html', {'passwd':thepasswd})

def home(request):
    time = str(datetime.datetime.now())
    return render(request, 'gen/home.html', {'timenow':time} )


def about(request):
    """Shows todays current time and date."""
    #today = datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")
    return render(request, 'gen/about.html')
