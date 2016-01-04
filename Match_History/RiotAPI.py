import json
import urllib2
import time
import re
from Match_History.models import champion, item, summonerSpell, summoner

#Adding custom header to urllib2 or else it's not authorized
opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'League of Legends Match History by spoonily')]

KEY = "Get your own at developer.riotgames.com"
REGION = "na"
BASE = "https://%s.api.pvp.net/api/lol/%s" % (REGION, REGION)
RECENT = "/v1.3/game/by-summoner/"
SUMMONER = "/v1.4/summoner/by-name/"
CHAMPION = "https://na.api.pvp.net/api/lol/static-data/%s/v1.2/champion/" % (REGION)
SPELLS = "https://na.api.pvp.net/api/lol/static-data/na/v1.2/summoner-spell?spellData=image&"
ITEM = "https://na.api.pvp.net/api/lol/static-data/na/v1.2/item?itemListData=image&"
CHAMPIMG = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/champion/"
IMG = "http://ddragon.leagueoflegends.com/cdn/5.22.3/img/item/"

#Gets summoner dictionary
def getSummoner (summonerName):
	urlSummoner = summonerName.replace(" ", "%20")
	url = "%s%s%s?%s" % (BASE, SUMMONER, urlSummoner, KEY)	
	result = getDict(url)

	return result

#Replaces spaces and lowercase for accessing in dictionary
def formatSummonerName (summonerName):
	summonerName = summonerName.lower()
	summonerName = summonerName.replace(" ", "")
	return summonerName

#Grabs ten most recent matches
def getRecentMatches (summonerID):
	url = "%s%s%s/recent?%s" % (BASE, RECENT, summonerID, KEY)
	result = getDict(url)
	return result["games"]

#Access url and converts json to dictionary
def getDict (url):
	try:
   		opener.open(url)
	except urllib2.HTTPError, err:
   		if err.code == 404 or err.code == 400:
   			dict = "404"
   		elif err.code == 401:
   			dict = "401"
   		elif err.code == 429:
   			dict = "429"
   		elif err.code == 500 or err.code == 503:
   			dict = "Server is Down, Try Again Later"
       	else:
       		dict = json.loads(opener.open(url).read())

	return dict

#Gets summoner name dictionary
def getSummonerName (summonerID):
	url = "%s/v1.4/summoner/%s/name/?%s" % (BASE, summonerID, KEY)
	dict = getDict(url)
	return dict

#Gets image url from SQL tables
def getImageUrl(championID):
	champ = champion.objects.get(ChampionID = championID)
	champURL = champ.ChampImg
	url = "%s%s" % (CHAMPIMG, champURL)
	return url

#Adds important champion information to SQL tables
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

#Sets up item tables
def setupSumms():
	summs = "%s%s" % (SPELLS, KEY)
	summs = getDict(item)['data']
	for i in summs:
		ID = summs[i]['id']
		name = summs[i]['name']
		img = summs[i]['image']['full']
		print ID
		print name
		print img
		summtable = summonerSpell()
		summtable.summID = ID
		summtable.summurl = img
		summtable.name = name
		summtable.save()

#Adds summoner spells to table
def setupItem():
	itemurl = "%s%s" % (ITEM, KEY)
	itemdict = getDict(itemurl)['data']
	for i in itemdict:
		description = itemdict[i]['description']
		description = description.replace('<br>', '\n')
		description = re.sub(r'\<[^>]*\>', "", description)
		print description
		ID = itemdict[i]['id']
		name = itemdict[i]['name']
		img = itemdict[i]['image']['full']
		print ID
		print name
		print img
		itemtable = item()
		itemtable.itemID = ID
		itemtable.itemUrl = img
		itemtable.itemName = name
		itemtable.itemDesc = description
		itemtable.save()		

#in case I want to set up tables again
#setupChampImage()
#in case I want to set up tables again
#setupItem()
#setup summoner spells
#setupSumms()