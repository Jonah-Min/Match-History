from django.contrib import admin

from .models import champion, item

class ChampsAdmin(admin.ModelAdmin):
	list_display = ('Champions')

class ItemsAdmin(admin.ModelAdmin):
	list_display = ('Items')

# Register your models here.
admin.site.register(champion)
admin.site.register(item)
