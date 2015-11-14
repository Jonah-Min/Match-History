import json
import urllib
import urllib2

KEY = "api_key=556973ba-ec24-4a67-8a7f-97272d28b50a"
REGION = "na"
BASE = "https://%s.api.pvp.net/api/lol/%s" % (REGION, REGION)
RECENT = "/v1.3/game/by-summoner/"
SUMMONER = "/v1.4/summoner/by-name/"
CHAMPION = "https://na.api.pvp.net/api/lol/static-data/%s/v1.2/champion/" % (REGION)

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
	print url
	result = getDict(url)
	return result["games"]

def getDict (url):
	dict = json.loads(urllib2.urlopen(url).read())
	return dict

def getSummonerName (summonerID):
	url = "%s/v1.4/summoner/%s/name/?%s" % (BASE, summonerID, KEY)
	dict = getDict(url)
	return dict

def getChampImage (championID):
	url = "%s%s?champData=image&%s" % (CHAMPION, championID, KEY)
	dict = getDict(url)
	sleep(.5);

	return $result;

#id = getSummoner("mk kraken")
#summonerName = getSummonerName("id")
#print summonerName

"""
<?php

		define("KEY", "api_key=556973ba-ec24-4a67-8a7f-97272d28b50a");
		define("REGION", "na");
		define("BASE", "https://" . REGION . ".api.pvp.net/api/lol/" . REGION);
		define("RECENT", "/v1.3/game/by-summoner/");
		define("SUMMONER", "/v1.4/summoner/by-name/");
		define("CHAMPION", "https://na.api.pvp.net/api/lol/static-data/". REGION . "/v1.2/champion/");

		function getSummoner ($summonerName) {
			$urlSummoner = rawurlencode($summonerName);
			$summonerName = formatSummonerName($summonerName);
			$url = BASE . SUMMONER . $urlSummoner . "?" . KEY;
			$result = getJson($url);

			return $result;
		}

		function getSummonerName ($summonerID) {
			$url = BASE . "/v1.4/summoner/" . $summonerID . "/name/?" . KEY;
			$result = getJson($url);
			sleep(1.5);

			$name = $result[$summonerID];
			return $name;
		}

		function getRecentGames ($id) {
			$url = BASE . RECENT . $id . "/recent?" . KEY;
			$result = getJson($url);

			return $result["games"];
		}

		function getJson ($url, $other=false, $static=false) {

			$json = @file_get_contents($url);
			$result = json_decode($json, True);
			return $result;

		}

		function formatSummonerName ($summonerName) {
			$summonerName = strtolower($summonerName);
			$summonerName = str_replace(" ", "", $summonerName);
			return $summonerName;
		}

		function getChampionName ($champID) {
			$url = CHAMPION . $champID . "?champData=image&" . KEY;
			$result = getJson($url);
			sleep(.5);

			return $result;

		}

?>
"""