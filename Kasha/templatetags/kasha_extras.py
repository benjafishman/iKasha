from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='keyvalue')
def keyvalue(d, key):
	key = str(key)
	try:
		return d[key]
	except (KeyError, IndexError, TypeError) as e:
		return ''
@register.filter(name='verseurl')
def verseurl(book, chapter, verse):
	return book + "/" + chapter + "/" + verse