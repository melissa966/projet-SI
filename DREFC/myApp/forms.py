from unittest.util import _MAX_LENGTH
from django import forms
from django.forms import ModelForm, models
from .models import Enseignants, Entreprise, MembreEntreprise, Stage, Stagiaire
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate
import email

from django.contrib.auth.models import User
class MembreForms (ModelForm):
    class Meta:
        model = MembreEntreprise
        fields ="__all__" 
    
    def __init__(self, *args, **kwargs):
        super(MembreForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    
class StageForms (ModelForm):
    class Meta:
        model = Stage
        fields ="__all__" 

    def __init__(self, *args, **kwargs):
        super(StageForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EntrepriseForms (ModelForm):
    class Meta:
        model = Entreprise
        fields ="__all__" 

    def __init__(self, *args, **kwargs):
        super(EntrepriseForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class EnseiganatForms (ModelForm):
    class Meta:
        model = Enseignants
        fields ="__all__" 
    
    def __init__(self, *args, **kwargs):
        super(EnseiganatForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class StagiaiareForms (ModelForm):
    class Meta:
        model = Stagiaire
        fields ="__all__" 

    def __init__(self, *args, **kwargs):
        super(StagiaiareForms, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'



class RegisterForms(UserCreationForm):
    email=forms.EmailField()
    class Meta:
        model = User
        fields =["username","password1","password2"]

        

