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

@register.filter(name = 'url')
def url(ChampionID):
	champ = champion.objects.get(ChampionID = ChampionID)
	champURL = champ.ChampImg
	url = "%s%s" % (CHAMPIMG, champURL)
	return url

@register.filter(name = 'summicon')
def summicon(iconID):
	if iconID < 0:
		url = "http://i.imgur.com/YwtIiZT.jpg"
	else:
		url = "%s%s.png" % (ICON, iconID)
	return url

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
		print summonername
		summ.save()
	else:
		summonerresult = summoner.objects.get(SummonerID = summonerID)
		summonername = summonerresult.SummonerName
	return summonername

@register.filter(name = 'format')
def formatGameType(gametype):
	toReturn = gametype.replace('_', ' ')
	if toReturn == "ARAM UNRANKED 5x5":
		toReturn = "ARAM"
	elif toReturn == "CAP 5x5":
		toReturn = "TEAM BUILDER"
	elif toReturn == "ONEFORALL 5x5":
		toReturn = "ONE FOR ALL"
	return toReturn

def getDict (url):
	dict = json.loads(urllib2.urlopen(url).read())
	return dict