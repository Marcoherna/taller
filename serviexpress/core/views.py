from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def inicio(request):
    return render(request, 'core/inicio.html') # agregado para apuntar cuando abra al index.html

