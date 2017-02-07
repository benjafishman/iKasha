from django.db import models
from django.contrib.postgres.fields import ArrayField, JSONField

class Question(models.Model):
	question_text = models.TextField(max_length=500)
	pub_date = models.DateTimeField('date published')
	he_verse_text = models.TextField(null=True, max_length=500, blank=True)
	en_verse_text = models.TextField(null=True, max_length=500, blank=True)
	book_source = models.CharField(null=True, max_length=500, blank=True)
	verses = ArrayField(models.CharField(max_length=200), blank=True)


	def __str__(self):
		return self.question_text

	class Meta:
		verbose_name = "Question"
		verbose_name_plural = "Questions"


class SourceQuestion(models.Model):
	book_chapter_sentence = models.CharField(max_length=100)
	question = models.ForeignKey(Question)


class BookChapterQuestions(models.Model):
	book_name = models.CharField(max_length=100)
	chapter = models.CharField(max_length=100)
	question_list =JSONField()	