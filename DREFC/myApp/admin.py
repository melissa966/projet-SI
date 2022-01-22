from django.contrib import admin
from myApp.models import  Stagiaire
from myApp.models import Entreprise, MembreEntreprise
from myApp.models import Enseignants
from myApp.models import Stage

# Register your models here.



# Register your models here.
admin.site.register(Stage)
admin.site.register(Enseignants)
admin.site.register(MembreEntreprise)
admin.site.register(Entreprise)
admin.site.register(Stagiaire)


