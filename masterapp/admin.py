from django.contrib import admin

from masterapp.models import Master, Profession, Dokument, CompletedWork

admin.site.register(Master)
admin.site.register(Profession)
admin.site.register(Dokument)
admin.site.register(CompletedWork)
