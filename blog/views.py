from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from blog.models import Article
from .forms import ContactForm, ConnexionForm, ArticleForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.urls import reverse
from django.utils.translation import ugettext as _
from django.utils.translation import ungettext
from django.utils import timezone
from django.contrib.auth.models import User


def date_actuelle(request):
    return render(request, 'blog/date.html', {'date': datetime.now()})

def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2
    return render(request, 'blog/addition.html', locals())

def accueil(request):
    article = Article.objects.all()
    return render(request, 'accueil.html', {'derniers_articles': article})

def lire(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'blog/lire.html', {'article':article})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid(): 
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        envoi = True
    
    return render(request, 'contact.html', locals())

def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user: 
                login(request, user)  
            else: 
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html', locals())

def deconnexion(request):
    logout(request)
    return redirect(reverse(accueil))

def test_i18n(request):
    nb_chats = 2
    couleur = "blanc"
    chaine = _("J'ai un %(animal)s %(col)s.") % {'animal': 'chat', 'col': couleur}
    infos = ungettext(
        "… et selon mes informations, vous avez %(nb)s chat %(col)s !",
        "… et selon mes informations, vous avez %(nb)s chats %(col)ss !",
        nb_chats) % {'nb': nb_chats, 'col': couleur}

    return render(request, 'test_i18n.html', locals())

def Nouvel_Article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST or None, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.date = timezone.now()
            article.save()
        return render(request, 'accueil.html', {'form': form})
    else:
        form = ArticleForm()
    return render(request, 'blog/nouvel_article.html', {'form': form})

def Modifier_Article(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == "POST":
        form = ArticleForm(request.POST or None, request.FILES, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.auteur = request.user
            article.date = timezone.now()
            article.save()
#            if User.is_authentified and User.username == article.auteur:
 #               article.auteur.is_connected = True
        return render(request, 'blog/lire.html', {'article': article})
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blog/modifier_article.html', {'form': form, 'article': article})


def bad_request(request, exception):
    return render(request, 'bad_request.html', locals())

def permission_denied(request, exception):
    return render(request, 'permission_denied.html', locals())

def page_not_found(request, exception):
    return render(request, 'page_not_found.html', locals())

def server_error(request):
    return render(request, 'server_error.html', locals())
