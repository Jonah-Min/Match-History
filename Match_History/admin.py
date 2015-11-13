from django.contrib import admin

from .models import summoner, champion

class SummonerAdmin(admin.ModelAdmin):
	list_display = ('Summoner')

class ChampsAdmin(admin.ModelAdmin):
	list_display = ('Champions')

# Register your models here.
admin.site.register(summoner)
admin.site.register(champion)