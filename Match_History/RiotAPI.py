import json
import urllib
import urllib2
import time
from Match_History.models import champion

KEY = "api_key=556973ba-ec24-4a67-8a7f-97272d28b50a"
REGION = "na"
BASE = "https://%s.api.pvp.net/api/lol/%s" % (REGION, REGION)
RECENT = "/v1.3/game/by-summoner/"
SUMMONER = "/v1.4/summoner/by-name/"
CHAMPION = "https://na.api.pvp.net/api/lol/static-data/%s/v1.2/champion/" % (REGION)
CHAMPIMG = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/champion/"

def getSummoner (summonerName):
	urlSummoner = summonerName.replace(" ", "%20")
	url = "%s%s%s?%s" % (BASE, SUMMONER, urlSummoner, KEY)	
	result = getDict(url)
	return result

def formatSummonerName (summonerName):
	summonerName = summonerName.lower()
	summonerName = summonerName.replace(" ", "")
	return summonerName

def getRecentMatches (summonerID):
	url = "%s%s%s/recent?%s" % (BASE, RECENT, summonerID, KEY)
	result = getDict(url)
	return result["games"]

def getDict (url):
	dict = json.loads(urllib2.urlopen(url).read())
	return dict

def getSummonerName (summonerID):
	url = "%s/v1.4/summoner/%s/name/?%s" % (BASE, summonerID, KEY)
	dict = getDict(url)
	return dict

def getImageUrl(championID):
	champ = champion.objects.get(ChampionID = championID)
	champURL = champ.ChampImg
	url = "%s%s" % (CHAMPIMG, champURL)
	return url

def setupChampImage ():
	champs = "%s/v1.2/champion?%s" % (BASE, KEY)
	ids = getDict(champs)['champions']
	for i in range(len(ids)):
		champId = ids[i]['id']
		url = "%s%s?champData=image&%s" % (CHAMPION, champId, KEY)
		dict = getDict(url)
		time.sleep(1)
		c = champion()
		c.ChampionID = ids[i]['id']
		c.ChampionName = dict['name']
		c.ChampImg = dict['image']['full']
		c.save()

	return dict;

print getImageUrl(112)

#id = getSummoner("mk kraken")
#summonerName = getSummonerName("id")
#print summonerName
#setupChampImage()

