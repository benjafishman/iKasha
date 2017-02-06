from django.db import models
from django.contrib.postgres.fields import ArrayField

class Question(models.Model):
	question_text = models.TextField(max_length=500)
	pub_date = models.DateTimeField('date published')
	he_verse_text = models.TextField(null=True, max_length=500, blank=True)
	en_verse_text = models.TextField(null=True, max_length=500, blank=True)
	book_source = models.CharField(null=True, max_length=500, blank=True)

	class Meta:
		verbose_name = "Question"
		verbose_name_plural = "Questions"
class SourceQuestion(models.Model):
	book_chapter_sentence = models.CharField(max_length=100)
	question = models.ForeignKey(Question)


