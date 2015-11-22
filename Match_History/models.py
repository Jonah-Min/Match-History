from django.db import models

# Create your models here.

#Summoner in League of Legends, has summonerID and summoner name
class summoner(models.Model):
	SummonerName = models.CharField(max_length=20)
	SummonerID = models.CharField(max_length=20, default="")

	def __unicode__ (self):
		return self.SummonerName

#Initializes all champions in the game with their name, ID, and their url for image
#Data is cached prior to running server to avoid rate limits
class champion(models.Model):
	ChampionName = models.CharField(max_length=100)
	ChampionID = models.CharField(max_length=20, default="")
	ChampImg = models.CharField(max_length=20, default="")

	def __unicode__ (self):
		return self.ChampionName	

#Caches every item in the game to avoid rate limits
class item(models.Model):
	itemName = models.CharField(max_length=100)
	itemID = models.CharField(max_length=20, default="")
	itemUrl = models.CharField(max_length=20, default="")
	itemDesc = models.CharField(max_length=200, default="")

	def __unicode__ (self):
		return self.itemName

#Caches every summoner spell to avoid rate limits
class summonerSpell(models.Model):
	name = models.CharField(max_length=100)
	summID = models.CharField(max_length=20, default="")
	summurl = models.CharField(max_length=50, default="")

	def __unicode__ (self):
		return self.name