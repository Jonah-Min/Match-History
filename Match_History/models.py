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

class item(models.Model):
	itemName = models.CharField(max_length=100)
	itemID = models.CharField(max_length=20, default="")
	itemUrl = models.CharField(max_length=20, default="")

	def __unicode__ (self):
		return self.itemName

class summonerSpell(models.Model):
	name = models.CharField(max_length=100)
	summID = models.CharField(max_length=20, default="")
	summurl = models.CharField(max_length=50, default="")

	def __unicode__ (self):
		return self.name