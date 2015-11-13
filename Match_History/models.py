from django.db import models

# Create your models here.
class summoner(models.Model):
	SummonerName = models.CharField(max_length=20)

	def __unicode__ (self):
		return self.SummonerName