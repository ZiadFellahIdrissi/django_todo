from django.shortcuts import render,redirect
from django.http import HttpResponse
from firstapp.models import Etudiant
from .models import Etudiant
# Create your views here.


def home(request):
    return render(request,"home.html")

def affiche_tableau_etudiant(request):
    return render(request,"tabEtudiant.html",{"etudiant": Etudiant.objects.all()}) 

def supprimer_etudiant(request):
    if request.method == 'POST':
        v_id =  request.POST['id'] 
        Etudiant.objects.filter(id=v_id).delete()
    return HttpResponse()

def modifier_etudiant(request):
    if request.method == 'POST':
        v_id =  request.POST['id'] 
        v_nom =  request.POST['nom'] 
        v_prenom =  request.POST['prenom']
        v_age =  request.POST['age']
        Etudiant.objects.filter(id=v_id).update(
            nom = v_nom,
            prenom = v_prenom,
            age_1 = v_age
        )
    return HttpResponse()

def ajouter_etudinat(request):
    if request.method == 'POST':
        v_nom =  request.POST['nom'] 
        v_prenom =  request.POST['prenom']
        v_age =  request.POST['age']
        Etudiant.objects.create(
            nom = v_nom,
            prenom = v_prenom,
            age_1 = v_age
        )
    return HttpResponse()