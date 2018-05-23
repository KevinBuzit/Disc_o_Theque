from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponse
from datetime import datetime
from ThequeAdmin.models import Music


# Create your views here.
def accueil(request):
    return render(request, 'ThequeAdmin/accueil.html', locals())

def list(request):
    musics = Music.objects.all()
    return render(request, 'ThequeAdmin/liste_cd.html', {'liste_musiques': musics})

def cd_detail(request, id_cd):
    musique = get_object_or_404(Music, id=id_cd)
    
    return render(request, 'ThequeAdmin/detail_cd.html', {'musique':musique})