"""DREFC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
