from django.contrib import admin
from django.urls import include, path
from myApp.views import index,stat, create ,createStage ,createEntreprise,createEnseiganat,createStagiaiare
from myApp import views as v
from myApp.views import deleteStage
from myApp.views import deleteStagiaire
from myApp.views import deleteEnseignant
from myApp.views import deleteEntreprise
from myApp.views import deleteEmployee
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('stats', stat , name='stat'),
    path('create', create, name="create"),
    path('createStage', createStage,name="createStage"),
    path('createEntreprise', createEntreprise ,name="createEntreprise"),
    path('createEnseiganat', createEnseiganat ,name="createEnseiganat"),
    path('createStagiaiare', createStagiaiare ,name="createStagiaiare"),
    path('',include("django.contrib.auth.urls")),
    path("register",v.register,name="register"),
    path('MembreEntreprise/delete/<int:idf>',deleteEmployee,name="deleteEmployee"),
    path('entreprise/delete/<int:idf>',deleteEntreprise,name="deleteEntreprise"),
    path('enseignant/delete/<str:idf>',deleteEnseignant,name="deleteEnseignant"),
    path('stagiaire/delete/<int:idf>',deleteStagiaire,name="deleteStagiaire"),
    path('stage/delete/<str:idf>',deleteStage,name="deleteStage")

]
