from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("""
        <h1>Bienvenue !</h1>
        <p>Voici la page de gestion de la médiathèque</p>
    """)