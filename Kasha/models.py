from django.db import models
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
	question_text = models.TextField(max_length=500)
	pub_date = models.DateTimeField('date published')
	he_verse_text = models.TextField(null=True, max_length=500, blank=True)
	en_verse_text = models.TextField(null=True, max_length=500, blank=True)
	book_source = models.CharField(null=True, max_length=500, blank=True)


class Source_Questions_Listing(models.Model):
	book_chapter_sentence = models.CharField(max_length=100)
	questions = ArrayField(models.CharField(max_length=200), blank=True)


