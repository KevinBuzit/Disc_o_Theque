from django.db import models

# Create your models here.
class Music(models.Model):
    nom_album = models.CharField(max_length=100, verbose_name="Nom de l'album")
    numero_piste = models.IntegerField(verbose_name="Numéro de la piste")
    titre = models.CharField(max_length=100)
    autheur = models.CharField(max_length=100, null=True)
    compositeur = models.CharField(max_length=100, null=True)
    interprete = models.CharField(max_length=100)
    url_pochette = models.URLField(verbose_name="Url de la pochette")

    class Meta:
        verbose_name = "music"
        ordering = ['nom_album']
    
    def __str__(self):
        """ 
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que 
        nous traiterons plus tard dans l'administration
        """
        return self.titre