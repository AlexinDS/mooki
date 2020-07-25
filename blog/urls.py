from django.urls import path
from . import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('article/<int:id>', views.lire, name='lire'),
    path('contact/', views.contact, name='contact'),
    path('connexion/', views.connexion, name='connexion'),
    path('deconnexion/', views.deconnexion, name='deconnexion'),
    path('nouvel_article/', views.Nouvel_Article, name='nouvel_article'),
    path('modifier_article/<int:id>', views.Modifier_Article, name='modifier_article'),
]
