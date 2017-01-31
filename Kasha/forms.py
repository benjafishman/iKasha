#forms.pyfrom django import forms
__author__ = 'benfishman'

from django import forms

from django.core import validators

class GetText(forms.Form):
	CHOICES = (
		('', 'Choose'),
		('Chumash', 'Chumash'),
		('Gemara', 'Gemara'),
		)
	torahType = forms.ChoiceField(choices = CHOICES, 
		widget=forms.Select(attrs={
		'id': 'myCustomId',
		'class': 'form-control',
		'name': 'myCustomName',
		'placeholder': 'Torah Text',
		"onChange":'changecat(this.value);'}
		), required=True)
	sefer = forms.CharField(
		widget=forms.Select(choices =[],attrs={
		'id': 'category',
		'class': 'form-control',
		'name': 'category',
		'placeholder': 'choose',
		"onChange":'changeper(this.value);'}
		), required=False)
	perek = forms.CharField(
		widget=forms.Select(choices =[], attrs={
		'id': 'perek',
		'class': 'form-control',
		'name': 'perek',
		'placeholder': 'choose',}
		), required=False)

	def clean(self):
		if self.cleaned_data['sefer'] is "" or self.cleaned_data['perek'] is "":
			print("here error")
			raise forms.ValidationError('Please input valid data')

			

