from django import forms

from Match_History.models import summoner

class summonerForm(forms.Form):
	summoner = forms.CharField(label='', max_length=20)

	def is_valid(self):
		return True