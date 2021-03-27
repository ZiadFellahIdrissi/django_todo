from django.db import models

# Create your models here.

class Etudiant(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    age_1 = models.IntegerField()

    # def __str__(self):
    #     return self.nom+' '+self.prenom,self.age_1
