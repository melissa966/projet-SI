from django.forms import ModelForm
from .models import Enseignants, Entreprise, MembreEntreprise, Stage, Stagiaire

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