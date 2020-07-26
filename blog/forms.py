from django import forms
from .models import Article, Categorie
from django.contrib.auth.models import User
from django.utils import timezone

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(label='Message')
    envoyeur = forms.EmailField(label="Votre adresse e-mail")

class ConnexionForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class ArticleForm(forms.ModelForm):
 #   photo = forms.ImageField()
    contenu = forms.CharField(widget=forms.Textarea(attrs={'class': 'textarea'}))
    class Meta:
        model = Article
        fields = ('titre', 'contenu','categorie') #, 'photo'
