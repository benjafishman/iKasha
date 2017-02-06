from django.db import models

class Question(models.Model):
	question_text = models.TextField(max_length=500)
	pub_date = models.DateTimeField('date published')
	he_verse_text = models.TextField(null=True, max_length=500, blank=True)
	en_verse_text = models.TextField(null=True, max_length=500, blank=True)
	book_source = models.CharField(null=True, max_length=500, blank=True)



