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

	form = data
	something = RiotAPI.getSummoner(form)

	return render(request, 'Match_History/result.html', {'form': form, 'something': something})