from django import forms

from Match_History.models import summoner

#Basic form for grabbing summoner name
class summonerForm(forms.Form):
	summoner = forms.CharField(label='', max_length=20)

	def is_valid(self):
		return True