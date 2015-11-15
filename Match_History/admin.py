from django.contrib import admin

from .models import summoner, champion, item

class SummonerAdmin(admin.ModelAdmin):
	list_display = ('Summoner')

class ChampsAdmin(admin.ModelAdmin):
	list_display = ('Champions')

class ItemsAdmin(admin.ModelAdmin):
	list_display = ('Items')

# Register your models here.
admin.site.register(summoner)
admin.site.register(champion)
admin.site.register(item)