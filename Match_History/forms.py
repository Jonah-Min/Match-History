from django import forms

#Basic form for grabbing summoner name
class summonerForm(forms.Form):
	summoner = forms.CharField(label='', 
		max_length=20, 
		widget=forms.TextInput(attrs={'placeholder': 'Summoner Name'}))

	def is_valid(self):
		return True
		