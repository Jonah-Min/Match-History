from django.shortcuts import render
from django.http import HttpResponse
from Match_History.forms import summonerForm
import RiotAPI

# Create your views here.
def index(request):
	form = summonerForm()
	
	return render(request, 'Match_History/index.html', {'form': form})

def result(request):

	# Grab summoner name from form when submitted
	if request.method == 'POST':
		form = summonerForm(request.POST)
		data = request.POST.get('summoner')

	# Grab summoner information
	summoner = data
	summonerName = RiotAPI.formatSummonerName(summoner)
	summonerDict = RiotAPI.getSummoner(summonerName)

	# Grab match data for summoner
	summonerID = summonerDict['accountId']
	summonerIcon = summonerDict['profileIconId']
	recentGames = RiotAPI.getRecentMatches(summonerID)

	length = len(recentGames)

	return render(request, 'Match_History/result.html', {
		'summoner': summoner,
		'id' : summonerID,
		'icon' : summonerIcon,
		'recent' : recentGames,
		'length' : length,
		'form' : form
	})
