from CLEI.apps.inscripciones.models import Participante, Inscripcion, \
    TipoDeInscripcion, TipoDeDescuento
from django.contrib import admin


admin.site.register(Inscripcion)
admin.site.register(Participante)
admin.site.register(TipoDeInscripcion)
admin.site.register(TipoDeDescuento)
# Register your models here.
