from django.contrib import admin

# Register your models here.
from .models import Word

class WorldAdmin(admin.ModelAdmin):
    word_display = ('word')

admin.site.register(Word, WorldAdmin)