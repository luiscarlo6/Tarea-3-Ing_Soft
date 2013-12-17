'''
Created on 14/12/2013

@author: HP
'''
from CLEI.apps.clei.models import MiembroCP, Articulo, Evaluacion
from django import forms


class RegistrarMiembroCP(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    class Meta:
        model = MiembroCP
        
    
    def clean(self):
        return self.cleaned_data
    
class RegistrarArticuloForm(forms.ModelForm):
    '''
    Clase para formulario de miembro de CP
    '''
    def __init__(self, *args, **kwargs):
        super(RegistrarArticuloForm, self).__init__(*args, **kwargs)
        self.fields['p2'].required = False
        self.fields['p3'].required = False
        self.fields['p4'].required = False
        self.fields['p5'].required = False
    class Meta:
        model = Articulo
        exclude = ('status',)
        
    
    def clean(self):
        
        return self.cleaned_data
    
class RegistrarEvaluacionForm(forms.ModelForm):
    '''
    Clase para formulario de evaluaciones
    '''
    class Meta:
        model = Evaluacion
        
    def clean(self):
        
        return self.cleaned_data
       
    
        
        