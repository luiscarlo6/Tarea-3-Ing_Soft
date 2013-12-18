from django import forms

from CLEI.apps.inscripciones.models import Participante, Inscripcion, AsistenciaGeneral

class RegistrarAsistenciaGeneralForm(forms.ModelForm):
    
    class Meta:
        model = AsistenciaGeneral
        #exclude = ('precio','beneficios','eventos')
            
    def clean(self):
        
        return self.cleaned_data      


class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        
class InscripcionForm(forms.ModelForm):
    class Meta:
        model = Inscripcion
