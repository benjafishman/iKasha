#forms.pyfrom django import forms
__author__ = 'benfishman'

from django import forms

from django.forms import ModelForm

from .models import Question

from django.core import validators

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

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

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		verses = forms.CharField(required=True)
		fields = ['question_text','pub_date', 'en_verse_text', 'book_source']


class QuestionBuilderForm(forms.Form):
	question_text = forms.CharField(
		label = "Kasha",
		max_length = 80,
		required = True,
		widget = forms.Textarea,
		)
	def __init__(self, *args, **kwargs):
		super(QuestionBuilderForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()	
		self.helper = FormHelper()
		self.helper.form_id = 'id-exampleForm'
		self.helper.form_class = 'blueForms'
		self.helper.form_method = 'post'
		self.helper.form_action = 'submit_survey'
		self.helper.add_input(Submit('submit', 'Submit'))

