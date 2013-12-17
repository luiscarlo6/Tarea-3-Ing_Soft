from django.contrib import admin

from CLEI.apps.clei.models import Persona, MiembroCP, Topico, Articulo, Evaluacion

admin.site.register(Persona)
admin.site.register(MiembroCP)
admin.site.register(Topico)
admin.site.register(Articulo)
admin.site.register(Evaluacion)