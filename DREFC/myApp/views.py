from django.shortcuts import render , redirect
from myApp.forms import StagiaiareForms
from myApp.forms import EnseiganatForms
from myApp.forms import EntrepriseForms
from myApp.forms import MembreForms ,StageForms
from .models import Enseignants, Entreprise, MembreEntreprise, Stage, Stagiaire
from .forms import RegisterForms
# Create your views here.


def index (request):
    varStage=Stage.objects.all()
    varEntreprise=Entreprise.objects.all()
    varMmembreEntreprise=MembreEntreprise.objects.all() 
    varEnseignant=Enseignants.objects.all()
    varStagiaire=Stagiaire.objects.all()
    return render(request,'index.html',{'varStage':varStage,'varEntreprise':varEntreprise,'varMmembreEntreprise':varMmembreEntreprise,'varEnseignant':varEnseignant,'varStagiaire':varStagiaire})



def create (request):
    if request.method =="POST":
        form= MembreForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  
        
    else:
        form=MembreForms
        return render(request,'create.html',{"form":form})

def createStage (request):
    if request.method =="POST":
        form= StageForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  
        
    else:
        form=StageForms
        return render(request,'createStage.html',{"form":form})

def createEntreprise (request):
    if request.method =="POST":
        form= EntrepriseForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  
        
    else:
        form=EntrepriseForms
        return render(request,'createStage.html',{"form":form})



def createEnseiganat (request):
    if request.method =="POST":
        form= EnseiganatForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  
        
    else:
        form=EnseiganatForms
        return render(request,'createEnseiganat.html',{"form":form})


def createStagiaiare (request):
    if request.method =="POST":
        form= StagiaiareForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")  
        
    else:
        form=StagiaiareForms
        return render(request,'createStagiaiare.html',{"form":form})




#new
def stat(request):
    stagess = Stage.objects.all()
    entr = Entreprise.objects.all()

    if request.method == "POST":
        form=StageForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("index1")
    else:
        form = StageForms    
    
    if request.method == "POST":
        form=EntrepriseForms(request.POST)
        if form.is_valid():
             form.save()
             form.save()
             return redirect("index1")
    else:
        form = EntrepriseForms 

    statistics = [0, 0, 0]
    for stage in stagess : 
        if stage.TypeStage == "1CS" :
            statistics[0] = statistics[0] + 1
        if stage.TypeStage == "3CS" :
            statistics[1] = statistics[1] + 1
        if stage.TypeStage == "1CPI" :
            statistics[2] = statistics[2] + 1
    
    statisticss = [0, 0, 0,0,0]
    for entreprise in entr : 
        if entreprise.Secteur_Entreprise == "telecommunication" :
            statisticss[0] = statisticss[0] + 1
        if entreprise.Secteur_Entreprise == "sante" :
            statisticss[1] = statisticss[1] + 1
        if entreprise.Secteur_Entreprise == "banque" :
            statisticss[2] = statisticss[2] + 1
        if entreprise.Secteur_Entreprise == "administration" :
            statisticss[3] = statisticss[3] + 1
        if entreprise.Secteur_Entreprise == "energie" :
            statisticss[4] = statisticss[4] + 1

        
    return render(request,'myApp/index1.html',{'statistics':statistics,'statisticss':statisticss,'entr':entr})



def deleteEmployee(request,idf):
    print(idf)
    instance = MembreEntreprise.objects.get(Id_Membre_Entreprise=idf)
    instance.delete()
    return redirect("/")

def deleteEntreprise(request,idf):
    print(idf)
    instance = Entreprise.objects.get(Id_Entreprise=idf)
    instance.delete()
    return redirect("/")

def deleteEnseignant(request,idf):
    print(idf)
    instance = Enseignants.objects.get(Nom_Enseignant=idf)
    instance.delete()
    return redirect("/")

def deleteStagiaire(request,idf):
    print(idf)
    instance = Stagiaire.objects.get(Matricule_Stagiaire=idf)
    instance.delete()
    return redirect("/")

def deleteStage(request,idf):
    print(idf)
    instance = Stage.objects.get(Titre_Projet=idf)
    instance.delete()
    return redirect("/")



def register(response):
    if response.method =="POST":
        form= RegisterForms(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/login")
    else:

        form = RegisterForms()
    return render(response,"register/register.html",{"form":form})