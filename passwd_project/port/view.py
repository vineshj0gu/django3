from django.shortcuts import render
from .models import proj

def home(request):
    projs = proj.objects.all()
    return render(request, 'port/home.html', {'projects':projs} )
