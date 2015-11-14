from django.db import models

# Create your models here.
class summoner(models.Model):
	SummonerName = models.CharField(max_length=20)
	SummonerID = models.CharField(max_length=20, default="")

	def __unicode__ (self):
		return self.SummonerName

class champion(models.Model):
	ChampionName = models.CharField(max_length=100)
	ChampionID = models.CharField(max_length=20, default="")
	ChampImg = models.CharField(max_length=20, default="")

	def __unicode__ (self):
		return self.ChampionName	