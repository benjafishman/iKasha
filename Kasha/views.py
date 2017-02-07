from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import GetText
from .models import Question, SourceQuestion

import pprint
import requests

#from <folder>.<filename> import <module>
from SefariaApi.SefariaApiChumashRashiManager import SefariaApiChumashRashiManager
from SefariaApi.sefaria_api_wrapper import SefariaApi

def index(request):
	if request.method == 'POST':
		form = GetText(request.POST)
		if form.is_valid():
			# Results = None properly clears any previous search results
			results = None

			# form data
			sefer = form.cleaned_data['sefer']
			perek = form.cleaned_data['perek']

			# create the api request suffix
			api_request_url = sefer + '.' + perek

			# instantiate sefaria api
			sefariaApi = SefariaApi()

			# make api request an return results
			text = sefariaApi.getText(api_request_url)

			# instantiate chumash manger 
			s1manager = SefariaApiChumashRashiManager(text)
			# return collated main text with rashi dictionary
			# TODO: error checking
			results = s1manager.getChumashRashi()

			# turn sefer form data to lower case for
			sefer = sefer.lower()
			# create sefer_perek string to query db for all questions with specified <sefer_perek>
			sefer_perek = sefer + "_" + perek
			# query DB for all q's with <sefer_perek>
			questions = SourceQuestion.objects.filter(book_chapter_sentence__startswith=sefer_perek)
			print(questions)

			pp = pprint.PrettyPrinter(indent=4)
			print("**************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************")
			#pp.pprint(results)
			form = GetText()
			return render(request, 'Kasha/index.html', {'form':form, 'results':results, 'sefer':sefer, 'perek':perek})
	else:
		form = GetText()		
	return render(request, 'Kasha/index.html', {'form':form})
	#return HttpResponse("Hello, world. You're at the Kasha index.")

def question_list(request, book, chapter, sentence):
	book = book.lower()
	bcs = book + "_" + chapter + "_" + sentence
	questions = SourceQuestion.objects.filter(book_chapter_sentence=bcs)
	return render(request, 'Kasha/questions_list.html', {'questions':questions, 'bcs':bcs})	

def question_detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'Kasha/question_detail.html', {'question':question})





