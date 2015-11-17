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
		if form.is_valid():
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
		return render(request, 'Match_History/kiara.html')
	elif summoner == "toona":
		summonerID = summonerDict[summonerName]['id']
		summonerIcon = "http://images1.houstonpress.com/imager/u/original/6417352/canned_tuna1.jpg"
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