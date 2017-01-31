__author__ = 'benfishman'

import requests
import pprint

class SefariaApi(object):
	BASE_API = 'http://www.sefaria.org/api/'
	SEFARIA_TEXT_TYPE= 'texts'

	def callApi(self, query_url):
		print(query_url)
		r = requests.get(query_url)
		if r.status_code == 200:
			return r
		else:
			raise ValueError(r.status_code)

	def getText(self, text):
		api_request = self.BASE_API + self.SEFARIA_TEXT_TYPE + '/'  + text
		r = self.callApi(api_request)
		return r

	def getRashi(self, text):
		RASHI_API = 'Rashi_on_'
		api_request = self.BASE_API + self.SEFARIA_TEXT_TYPE + '/' + RASHI_API + text
		r = self.callApi(api_request)
		return r
