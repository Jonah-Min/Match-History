from django.shortcuts import render
from django.http import HttpResponse
from Match_History.forms import summonerForm
import RiotAPI

# Create your views here.
def index(request):
	form = summonerForm()
	
	return render(request, 'Match_History/index.html', {'form': form})

def result(request):

	if request.method == 'POST':
		form = summonerForm(request.POST)
		data = request.POST.get('summoner')

	summoner = data
	summonerName = RiotAPI.formatSummonerName(summoner)
	summonerDict = RiotAPI.getSummoner(summonerName)

	if summonerDict == "404":
		summonerID = summoner
		summonerIcon = -1
		recentGames = []
		error = summonerDict
		length = 0
	elif summonerDict == "401":
		summonerID = summoner
		summonerIcon = -1
		recentGames = []
		error = summonerDict
		length = 0
	elif summonerDict == "429":
		summonerID = summoner
		summonerIcon = -1
		recentGames = []
		error = "Rate Limit Exceeded, Try Again Later"
		length = 0
	elif summonerDict == "Server is Down, Try Again Later":
		summonerID = summoner
		summonerIcon = -1
		recentGames = []
		error = summonerDict
		length = 0
	elif summoner == "acepie":
		summonerID = summonerDict[summonerName]['id']
		summonerIcon = "http://static.dnaindia.com/sites/default/files/2015/10/02/361285-john-cena-2.jpg"
		recentGames = RiotAPI.getRecentMatches(summonerID)
		length = len(recentGames)
		error = ""
	elif summoner == "rouged":
		summonerID = summonerDict[summonerName]['id']
		summonerIcon = "https://pmcdeadline2.files.wordpress.com/2013/02/minion__130211164715.jpg"
		recentGames = RiotAPI.getRecentMatches(summonerID)
		length = len(recentGames)
		error = ""
		return render(request, 'Match_History/kiara.html', {'summoner': summoner,
			'error' : error,
			'id' : summonerID,
			'icon' : summonerIcon,
			'recent' : recentGames,
			'length' : length,
			'form' : form})
	elif summoner == "toona":
		summonerID = summonerDict[summonerName]['id']
		summonerIcon = "http://freesamples2fillupyourmailbox.com/wp-content/uploads/2015/04/morton.jpg"
		recentGames = RiotAPI.getRecentMatches(summonerID)
		length = len(recentGames)
		error = ""
	else:
		summonerID = summonerDict[summonerName]['id']
		summonerIcon = summonerDict[summonerName]['profileIconId']
		recentGames = RiotAPI.getRecentMatches(summonerID)
		length = len(recentGames)
		error = ""

	return render(request, 'Match_History/result.html', {'summoner': summoner,
		'error' : error,
		'id' : summonerID,
		'icon' : summonerIcon,
		'recent' : recentGames,
		'length' : length,
		'form' : form})