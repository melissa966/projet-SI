from django.shortcuts import render , redirect
from myApp.forms import StagiaiareForms
from myApp.forms import EnseiganatForms
from myApp.forms import EntrepriseForms
from myApp.forms import MembreForms ,StageForms
from .models import Enseignants, Entreprise, MembreEntreprise, Stage, Stagiaire
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


    return render(request,'myApp/index1.html',{'statistics':statistics,'entr':entr})