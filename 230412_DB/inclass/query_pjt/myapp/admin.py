from django.contrib import admin

# Register your models here.
from .models import PetSitter, Pet

admin.site.register(Pet)
admin.site.register(PetSitter)