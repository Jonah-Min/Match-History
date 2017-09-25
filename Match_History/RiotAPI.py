import json
import requests
import time
import re
from Match_History.models import champion, item, summonerSpell

# User Agent header for Riot API request
HEADER = {
	'User-Agent': 'Match History by spoonily'
}

KEY = "api_key=RGAPI-9340ea1f-5721-4325-854c-6a8e9b0f715e"
VERSION = "v3"
BASE = "https://na1.api.riotgames.com/lol/"

# URL for API call to access information required for a match history
MATCHLIST = "match/%s/matchlists/by-account/" % (VERSION)
MATCHES = 'match/%s/matches/' % (VERSION)
SUMMONER = "summoner/%s/summoners/by-name/" % (VERSION)
CHAMPION = "https://na1.api.riotgames.com/lol/static-data/v3/champions/"
ITEM = "https://na1.api.riotgames.com/lol/static-data/v3/items/"

# Base link for retreiving images for static objects (item and champion images)
CHAMPIMG = "http://ddragon.leagueoflegends.com/cdn/7.17.2/img/champion/"
ITEMIMG = "http://ddragon.leagueoflegends.com/cdn/7.17.2/img/item/"


# Retrieves basic summoner information based off of summoner name,
# This grabs the account ID to allow for accessing match history for the account
#
# @param summonerName username of player
#
# @returns dictionary with basic user information
def getSummoner (summonerName):
	urlSummoner = summonerName.replace(" ", "%20")
	url = "%s%s%s?%s" % (BASE, SUMMONER, urlSummoner, KEY)	
	result = getDict(url)

	return result

# Formats players username so that information can be correctly grabbed from the API
# The API not allow for spaces and uppercase values
#
# @param summonerName username of player
#
# @returns username without spaces or uppercase letters
def formatSummonerName (summonerName):
	summonerName = summonerName.lower()
	summonerName = summonerName.replace(" ", "")

	return summonerName

# Grabs all relevant information from the past 15 matches
# Information grabbed includes KDA, summoner names of players, summoner spells,
# champion played, and items bought
#
# @param summonerID id of player 
#
# @returns dictionary of information on all players and user that was searched
def getRecentMatches (summonerID):
	url = "%s%s%s?%s" % (BASE, MATCHLIST, summonerID, KEY)

	result = getDict(url)
	matchList = result['matches'][:15]
	matchData = []

	for match in matchList:
		matchId = match['gameId']
		gameData = getMatchData(matchId)

		match['gameDuration'] = gameData['gameDuration']
		match['gameMode'] = gameData['gameMode']

		participants = gameData['participantIdentities']
		stats = gameData['participants']
		championId = match['champion']

		userData = {}

		# I can't seem to grab specific summoner information for a given game
		# So I check the id of the champ played with the participants and grab
		# statistics from that
		for i in range(10):
			if stats[i]['championId'] == championId:
				userData['championId'] = championId
				userData['win'] = stats[i]['stats']['win']
				userData['kills'] = stats[i]['stats']['kills']
				userData['deaths'] = stats[i]['stats']['deaths']
				userData['assists'] = stats[i]['stats']['assists']
				userData['item0'] = stats[i]['stats']['item0']
				userData['item1'] = stats[i]['stats']['item1']
				userData['item2'] = stats[i]['stats']['item2']
				userData['item3'] = stats[i]['stats']['item3']
				userData['item4'] = stats[i]['stats']['item4']
				userData['item5'] = stats[i]['stats']['item5']
				userData['item6'] = stats[i]['stats']['item6']
				userData['spell1'] = stats[i]['spell1Id']
				userData['spell2'] = stats[i]['spell2Id']

		match['teams'] = getTeamData(participants, stats)
		match['user'] = userData

		matchData.append(match)

	return matchData

# Retrieves information on all players in a given match
# Separates into blue and red team based off of team ID
#
# @param participants Basic information on all players in the game
# @param stats Stastic information of all players based off of participant ID
#
# @returns dictionary separating red and blue team with relevant information
def getTeamData(participants, stats):
	redTeam = []
	blueTeam = []

	for i in range(10):
		playerData = {}

		playerData['summonerName'] = participants[i]['player']['summonerName']
		playerData['championId'] = stats[i]['championId']
		playerData['kills'] = stats[i]['stats']['kills']
		playerData['deaths'] = stats[i]['stats']['deaths']
		playerData['assists'] = stats[i]['stats']['assists']
		playerData['item0'] = stats[i]['stats']['item0']
		playerData['item1'] = stats[i]['stats']['item1']
		playerData['item2'] = stats[i]['stats']['item2']
		playerData['item3'] = stats[i]['stats']['item3']
		playerData['item4'] = stats[i]['stats']['item4']
		playerData['item5'] = stats[i]['stats']['item5']
		playerData['item6'] = stats[i]['stats']['item6']
		playerData['spell1'] = stats[i]['spell1Id']
		playerData['spell2'] = stats[i]['spell2Id']

		if stats[i]['teamId'] == 100:
			blueTeam.append(playerData)
		else:
			redTeam.append(playerData)

	teams = {}
	teams['redTeam'] = redTeam
	teams['blueTeam'] = blueTeam

	return teams

# Makes quick API call to grab data about a single match
#
# @param matchId ID of a given match
#
# @returns dictionary with information on all players and game data for given match ID
def getMatchData(matchId):
	url = '%s%s%s?%s' % (BASE, MATCHES, matchId, KEY)
	result = getDict(url)

	return result

# Makes API call
def getDict (url):
   	dict = requests.get(url, headers=HEADER)

	return dict.json()

# Updates chamption image database table so that I can grab champion data for a given 
# champ ID without making mutliple API calls
def setupChampImage ():
	champUrl = "%s?%s&locale=en_US&tags=image&dataById=false" % (CHAMPION, KEY)
	champs = getDict(champUrl)['data']
	keys = champs.keys()

	for champ in keys:
		champId = champs[champ]['id']
		championName = champs[champ]['name']
		imageUrlName = champs[champ]['image']['full']

		c = champion()
		c.ChampionID = champId
		c.ChampionName = championName
		c.ChampImg = "%s%s" % (CHAMPIMG, imageUrlName)
		c.save()

# Updates items SQLlite table so that item information can be grabbed without making
# multiple API calls
def setupItem():
	itemurl = "%s?%s" % (ITEM, KEY)
	itemdict = getDict(itemurl)['data']
	keys = itemdict.keys()

	for itemId in keys:
		if not 'description' in itemdict[itemId].keys():
			continue

		description = itemdict[itemId]['description']
		description = description.replace('<br>', '\n')
		description = re.sub(r'\<[^>]*\>', "", description)

		ID = itemId
		name = itemdict[itemId]['name']
		img = "%s%s.png" % (ITEMIMG, ID)

		print ID
		print name
		print img

		itemtable = item()
		itemtable.itemID = ID
		itemtable.itemUrl = img
		itemtable.itemName = name
		itemtable.itemDesc = description
		itemtable.save()		

# setupChampImage()
# setupItem()
