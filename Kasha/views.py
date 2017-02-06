from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import GetText
from .models import Question

import pprint
import requests


#from <folder>.<filename> import <module>

from SefariaApi.SefariaApiChumashRashiManager import SefariaApiChumashRashiManager
from SefariaApi.sefaria_api_wrapper import SefariaApi
# Create your views here.
def index(request):
	if request.method == 'POST':
		form = GetText(request.POST)
		if form.is_valid():
			results = None
			sefer = form.cleaned_data['sefer']
			perek = form.cleaned_data['perek']
			api_request_url = sefer + '.' + perek
			
			# call sefaria api
			sefariaApi = SefariaApi()
			#print(sefariaApi)
			text = sefariaApi.getText(api_request_url)
			s1manager = SefariaApiChumashRashiManager(text)
			results = s1manager.getChumashRashi()
			pp = pprint.PrettyPrinter(indent=4)
			print("**************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************")
			#pp.pprint(results)
			form = GetText()
			return render(request, 'Kasha/index.html', {'form':form, 'results':results, 'sefer':sefer, 'perek':perek})
	else:
		form = GetText()		
	return render(request, 'Kasha/index.html', {'form':form})
	#return HttpResponse("Hello, world. You're at the Kasha index.")

def detail(request, question_id):
	print("here1")
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'Kasha/question.html')	







