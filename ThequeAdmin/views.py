from django.shortcuts import render
from django.http import Http404, HttpResponse
from datetime import datetime


# Create your views here.
def accueil(request):
    return render(request, 'ThequeAdmin/accueil.html', locals())

def list(request):
    return render(request, 'ThequeAdmin/liste_cd.html', locals())

def cd_detail(request, id_cd):
    return render(request, 'ThequeAdmin/detail_cd.html', locals())