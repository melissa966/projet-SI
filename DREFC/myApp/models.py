from pickle import TRUE
from pyexpat import model
from tkinter import CASCADE
from django.db import models

# Create your models here.
class MembreEntreprise(models.Model):
    Id_Membre_Entreprise=models.PositiveIntegerField(primary_key=True)
    Fonction_Membre_Entreprise=models.CharField(max_length=50,null=False)
    Nom_Membre_Entreprise=models.CharField(max_length=50,null=False)
    Prenom_Membre_Entreprise=models.CharField(max_length=50,null=False)
    Mail_Membre_Entreprise=models.EmailField(max_length=254)
    Nom_Entreprise=models.ForeignKey("Entreprise",on_delete=models.SET_NULL,null=TRUE,blank=True)
    stagee=models.ForeignKey("Stage",on_delete=models.SET_NULL,null=TRUE,blank=True)
    
    def __str__(self):
        return '| Employer : '+ self.Nom_Membre_Entreprise+' '+self.Prenom_Membre_Entreprise+'| Entreprise : '+str(self.Nom_Entreprise) 

    

class Stage(models.Model):
    TypeStage=models.CharField(max_length=4,null=False,blank=False)
    Titre_Projet=models.CharField(max_length=50,default="",null=False, unique=True)
    DateDeb_Stage= models.fields.DateField()
    DateDepot_Stage=models.fields.DateField()
    Note_Projet=models.PositiveBigIntegerField()
    membre_Entreprise_encadreur=models.ForeignKey("MembreEntreprise",on_delete=models.SET_NULL,null=TRUE,blank=True)
    Enseignant_promoteur=models.ForeignKey("Enseignants",on_delete=models.SET_NULL,null=TRUE,blank=True)
    grp_etd=models.ManyToManyField("Stagiaire",related_name="FaitPar")
    EvoluerM=models.ManyToManyField("MembreEntreprise",related_name="evoluer")
    EvoluerE=models.ManyToManyField("Enseignants",related_name="evoluerPar")
    
    def __str__(self):
        return 'Type de stage :'+ self.TypeStage+' | Titre du projet : '+self.Titre_Projet



class Entreprise(models.Model):
    Id_Entreprise=models.PositiveIntegerField(primary_key=True)
    Nom_Entreprise=models.CharField(max_length=40,default="",null=False)
    Adresse_Entreprise=models.CharField(max_length=50,null=False)
    Secteur_Entreprise=models.CharField(max_length=50,null=False)
    
    def __str__(self):
        return self.Nom_Entreprise+' | Adresse :'+ self.Adresse_Entreprise+' | Secteur :'+ self.Secteur_Entreprise


class Enseignants(models.Model):
    Nom_Enseignant=models.CharField(max_length=20,null=False)
    Prenom_Enseignant=models.CharField(max_length=20,null=False)
    Grade_Enseignant=models.CharField(max_length=20,null=False)
    Universit??=models.CharField(max_length=20,null=False)
    Mail_ens=models.EmailField(max_length=254)

    def __str__(self):
        return self.Nom_Enseignant+' '+self.Prenom_Enseignant


class Stagiaire (models.Model):
    Matricule_Stagiaire= models.PositiveIntegerField(primary_key=True)
    Specialite_Stagiaire=models.CharField(max_length=20,null=False,blank=False)
    Prenom_Stagiaire=models.CharField(max_length=50)
    Nom_Stagiaire=models.CharField(max_length=30)
    universit??=models.CharField(max_length=30)
    Datenaiss_Stagiaire=models.DateField()
    Lieunaiss_Stagiaire=models.CharField(max_length=20,null=False,blank=False)
    Mail=models.EmailField(max_length=254)
    def __str__(self):
        return 'Matricule : '+str(self.Matricule_Stagiaire)+' |Nom et Prenom : '+self.Nom_Stagiaire+' '+self.Prenom_Stagiaire+ ' | Universit?? : '+self.universit??


        



