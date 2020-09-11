from django.contrib import admin
from .models import Todo

class Todoadmin(admin.ModelAdmin):
    readonly_fields =('Created',)

admin.site.register(Todo, Todoadmin)
