import json
import urllib2

KEY = "api_key=556973ba-ec24-4a67-8a7f-97272d28b50a"
REGION = "na"
BASE = "https://%s.api.pvp.net/api/lol%s" % (REGION, REGION)
RECENT = "/v1.4/summoner/by-name/"
SUMMONER = "/v1.4/summoner/by-name/"

def getSummoner (summonerName):
	urlSummoner = urllib2.urlencode(summonerName)
	summonerName = formatSummonerName(summonerName)
	url = "%s%s%s?%s" % (BASE, SUMMONER, urlSummoner, KEY)
	result = json.loads(urllib2.urlopen(url).read())
	return result

def formatSummonerName (summonerName):
	summonerName = summonerName.lower()
	summonerName = summonerName.replace(" ", "")
	return summonerName


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