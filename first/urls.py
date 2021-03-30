"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('ajax/affiche_tableau_etudiant/', views.affiche_tableau_etudiant, name="affiche_tableau_etudiant"),
    path('ajax/ajouter_etudiant0/', views.ajouter_etudinat, name="ajouter_etudiant0"),
    path('ajax/suprimer_etudiant/',views.supprimer_etudiant),
    path('ajax/modifier_etudiant/',views.modifier_etudiant),
    path('ajax/donnee_etudiant/',views.donnee_etudiant)
]
