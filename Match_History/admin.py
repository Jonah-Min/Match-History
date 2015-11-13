from django.contrib import admin

from .models import summoner

class SummonerAdmin(admin.ModelAdmin):
	list_display = ('Summoner')

# Register your models here.
admin.site.register(summoner)