from django import forms

from .models import Country

class CountryForm(forms.Form):
	country_name = forms.CharField(label='Country Name', max_length=100)
	capital_city = forms.CharField(label='Capital City', max_length=100)
	description = forms.CharField(label='Description', max_length=2000)
	selected_states = forms.CharField(label='Selected States', max_length=400)
