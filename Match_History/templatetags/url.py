from django import template
from Match_History.models import champion, item, summonerSpell
import json
import time
import requests

# Base URLS for grabbing static image data
ICON = "http://ddragon.leagueoflegends.com/cdn/7.17.2/img/profileicon/"
SPELL = "http://ddragon.leagueoflegends.com/cdn/7.17.2/img/spell/"

register = template.Library()

# Formats game length time to the correct minute seconds format
@register.filter(name = 'timeformat')
def formatTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	time = "%d:%02d" % (minutes, seconds)

	return time

# Grabs urls for champion imagees
@register.filter(name = 'champImage')
def champImage(ChampionID):
	champ = champion.objects.filter(ChampionID = ChampionID)
	champUrl = "http://hex-color.com/images/1F2B2A.jpg"

	if champ:
		champ = champion.objects.get(ChampionID = ChampionID)
		champURL = champ.ChampImg

	return champURL

# Grabs icon for summoner spell
@register.filter(name = 'summicon')
def summicon(iconID):
	url = "%s%s.png" % (ICON, iconID)

	return url

#Grabs image link for summoner spells
@register.filter(name = 'summspell')
def summSpell(iconID):
	query = summonerSpell.objects.filter(summID = iconID)
	name = summonerSpell.objects.get(summID = iconID)
	imgName = name.summurl
	url = "%s%s" % (SPELL, imgName)
	
	return url

# Grabs image url of item
# Default image for when item is missing
@register.filter(name = 'itemimg')
def itemurl(itemID):
	itemobj = item.objects.filter(itemID = itemID)
	if not itemobj:
		itemURL = "http://www.colorhexa.com/1f2b2a.png"
	else:
		itemobj = item.objects.get(itemID = itemID)
		itemURL = itemobj.itemUrl

	return itemURL

# Grabs descritpion for item unless there is no item
@register.filter(name = "desc")
def getDesc(itemID):
	itemobj = item.objects.filter(itemID = itemID)
	if not itemobj:
		toReturn = ""
	else:
		itemobj = item.objects.get(itemID = itemID)
		itemDesc = itemobj.itemDesc
		itemName = itemobj.itemName
		toReturn = "%s\n\n%s" % (itemName, itemDesc)
	return toReturn

# Grabs champion name from tables based off id
@register.filter(name = 'name')
def getChampName(champID):
	champ = champion.objects.filter(ChampionID = champID)
	if not champ:
		name = "Champion not found"
	else:
		champ = champion.objects.get(ChampionID = champID)
		name = champ.ChampionName
	return name
