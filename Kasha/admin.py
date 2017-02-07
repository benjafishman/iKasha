from django.contrib import admin

from .models import Question, SourceQuestion

class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text', 'en_verse_text','he_verse_text','book_source','tags']
	list_display = ('question_text', 'verses','pub_date')
admin.site.register(Question, QuestionAdmin)



class SourceQuestionAdmin(admin.ModelAdmin):
	list_display = ['book_chapter_sentence']
admin.site.register(SourceQuestion, SourceQuestionAdmin)

