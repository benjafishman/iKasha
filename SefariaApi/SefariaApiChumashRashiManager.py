__author__ = 'benfishman'


import pprint
class SefariaApiChumashRashiManager(object):

	SEFARIA_API_QUERYSET = None

	def __init__(self, queryset):
		self.SEFARIA_API_QUERYSET = queryset

	def getRashi(self):
		# list comprehension to grab all rashi elements from the list of commentaries
		rashis = [d for d in self.SEFARIA_API_QUERYSET.json()['commentary'] if d['commentator'] == 'Rashi']
		#print(rashis)
		rashi_dict = {}
		# loop through rashis and create JSON elements for each one
		if rashis:
			for r in rashis:
				rashiItem = {
				'he': r['he'],
				'en': r['text'],
				'ref': r['sourceRef']}

				index = 1
				if not r['anchorVerse'] in rashi_dict:
					index=1
					rashi_dict[r['anchorVerse']] = {}
				else:
					while index in rashi_dict[r['anchorVerse']]:
						index+=1
				rashi_dict[r['anchorVerse']][index] = rashiItem
		return rashi_dict

	def getMainContent(self):
		# parse result for hebrew main text
		hebrew_content = self.SEFARIA_API_QUERYSET.json()["he"]

		# parse result for english main text
		english_content = self.SEFARIA_API_QUERYSET.json()["text"]

		# put english and hebrew main text in dictionary for return
		return {'en': english_content, 'he':hebrew_content}

	def getChumashRashi(self):
		
		chumash_rashi_dict = {}
		
		pasukNum = 1
		
		# Get dictionary of main content
		main_content = self.getMainContent()
		# Check if main content is not None
		if main_content is None:
			return (1,"Invalid Main Content")

		# Get dictionary of Rashis
		rashi_dict = self.getRashi()
		# Check if Rashi content is not None
		if rashi_dict is None:
			return (1,"Invalid Rashi Content")

		for pasuk in main_content["en"]:
						
			# Set rashi from the rashi dictionary but default to None
			rashi = None
			if pasukNum in rashi_dict:
					rashi = rashi_dict[pasukNum]
						
			element = {
			"he": main_content["he"][pasukNum-1],
			"en": main_content["en"][pasukNum-1],
			"rashi": rashi
			}
						
			chumash_rashi_dict[pasukNum] = element
						
			pasukNum+=1

		pp = pprint.PrettyPrinter(indent=4)
		pp.pprint(chumash_rashi_dict)

		return chumash_rashi_dict











