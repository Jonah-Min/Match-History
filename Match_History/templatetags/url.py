from django import template
from Match_History.models import champion, summoner, item, summonerSpell
import json
import time
import urllib2

CHAMPIMG = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/champion/"
ITEM = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/item/"
ICON = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/profileicon/"
SPELL = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/spell/"
KEY = "api_key=556973ba-ec24-4a67-8a7f-97272d28b50a"
REGION = "na"
BASE = "https://%s.api.pvp.net/api/lol/%s" % (REGION, REGION)

register = template.Library()

#Formats game length time
@register.filter(name = 'timeformat')
def formatTime(seconds):
	minutes, seconds = divmod(seconds, 60)
	time = "%d:%02d" % (minutes, seconds)
	return time

#Using Champion ID, grabs url for image
@register.filter(name = 'url')
def url(ChampionID):
	champ = champion.objects.get(ChampionID = ChampionID)
	champURL = champ.ChampImg
	url = "%s%s" % (CHAMPIMG, champURL)
	return url

#Grabs summoner icon image url
@register.filter(name = 'summicon')
def summicon(iconID):
	if iconID < 0:
		url = "http://i.imgur.com/YwtIiZT.jpg"
	elif isinstance(iconID, str):
		url = iconID
	else:
		url = "%s%s.png" % (ICON, iconID)
	return url

#Grabs image link for summoner spells
@register.filter(name = 'summspell')
def summSpell(iconID):
	query = summonerSpell.objects.filter(summID = iconID)
	if not query:
		url = "http://hex-color.com/images/1F2B2A.jpg"
	else:
		name = summonerSpell.objects.get(summID = iconID)
		imgName = name.summurl
		url = "%s%s" % (SPELL, imgName)
	return url

#Grabs image url of item
#Default image for when item is missing
@register.filter(name = 'itemimg')
def itemurl(itemID):
	itemobj = item.objects.filter(itemID = itemID)
	if not itemobj:
		url = "http://hex-color.com/images/1F2B2A.jpg"
	else:
		itemobj = item.objects.get(itemID = itemID)
		itemURL = itemobj.itemUrl
		url = "%s%s" % (ITEM, itemURL)
	return url

#Grabs summoner name, if it doesn't exist in the tables, adds new entry
@register.filter(name = 'summ')
def getSummName(summonerID):
	query = summoner.objects.filter(SummonerID = summonerID)
	if not query:
		url = "%s/v1.4/summoner/%s/name/?%s" % (BASE, summonerID, KEY)
		dict = getDict(url)
		time.sleep(1)
		summonername = dict[str(summonerID)]
		summ = summoner()
		summ.SummonerName = summonername
		summ.SummonerID = summonerID
		summ.save()
	else:
		summonerresult = summoner.objects.get(SummonerID = summonerID)
		summonername = summonerresult.SummonerName
	return summonername

#Removes underscores, also has several special edges cases for the constants
@register.filter(name = 'format')
def formatGameType(gametype):
	toReturn = gametype.replace('_', ' ')
	if toReturn == "ARAM UNRANKED 5x5":
		toReturn = "ARAM"
	elif toReturn == "CAP 5x5":
		toReturn = "TEAM BUILDER"
	elif toReturn == "ONEFORALL 5x5":
		toReturn = "ONE FOR ALL"
	elif toReturn == "ODIN UNRANKED":
		toReturn = "TWISTED TREELINE"
	elif toReturn == "NONE":
		toReturn = "CUSTOM"
	return toReturn

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

#Grabs api json result and converts to dictionary
def getDict (url):
	dict = json.loads(urllib2.urlopen(url).read())
	return dict


