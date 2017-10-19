from django.contrib import admin
from .models import Verb


class VerbAdmin(admin.ModelAdmin):
    pass


admin.site.register(Verb, VerbAdmin)
