from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom

class Article(models.Model):
    auteur = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titre = models.CharField(max_length=15)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    contenu = models.TextField()
    date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.date = timezone.now()
        self.save()

    def __str__(self):
        return self.titre
