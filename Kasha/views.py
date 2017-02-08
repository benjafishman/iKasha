from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .forms import GetText
from .models import Question, SourceQuestion, BookChapterQuestions

import pprint
import requests

#from <folder>.<filename> import <module>
from SefariaApi.SefariaApiChumashRashiManager import SefariaApiChumashRashiManager
from SefariaApi.sefaria_api_wrapper import SefariaApi

def index(request):
	if request.method == 'POST':
		form = GetText(request.POST)
		if form.is_valid():
			# Results = None => properly clears any previous search results
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
			chumash_rashi = s1manager.getChumashRashi()

			# turn sefer form data to lower case for
			sefer = sefer.lower()
			# create sefer_perek string to query db for all questions with specified <sefer_perek>
			sefer_perek = sefer + "_" + perek
			# query DB for all q's with <sefer_perek>
			book_chapter = BookChapterQuestions.objects.filter(book_name=sefer, chapter=perek)
			verses = None
			#print(book_chapter[0].verses)
			
			if book_chapter and book_chapter[0].verses:
				verses = book_chapter[0].verses

			pp = pprint.PrettyPrinter(indent=4)
			print("**************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************")
			pp.pprint(verses)
			
			#print(type(verses))
			#print(type(chumash_rashi))

			form = GetText()
			return render(request, 'Kasha/index.html', {'form':form, 'chumash_rashi':chumash_rashi, 'sefer':sefer, 'perek':perek, 'verses': verses})
	else:
		form = GetText()		
	return render(request, 'Kasha/index.html', {'form':form})

def question_list(request, book, chapter, sentence):
	book = book.lower()
	bcs = book + "." + chapter + "." + sentence
	questions = Question.objects.filter(verses__overlap=[bcs])
	return render(request, 'Kasha/questions_list.html', {'questions':questions, 'bcs':bcs})	

def question_detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	return render(request, 'Kasha/question_detail.html', {'question':question})





