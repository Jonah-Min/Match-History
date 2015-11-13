from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return render(request, 'Match_History/index.html')

def result(request):
	return render(request, 'Match_History/result.html')