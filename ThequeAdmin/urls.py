from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name="accueil"),
    path('liste', views.list, name="afficher_liste"),
    path('detail/<int:id_cd>', views.cd_detail, name="afficher_detail"),
]