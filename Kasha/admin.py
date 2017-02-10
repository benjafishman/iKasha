from django.contrib import admin

from .models import Question, Answer, BookChapterQuestions, SourceQuestion


class AnswerInline(admin.TabularInline):
	model = Answer
	extra = 1


class QuestionAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question_text', 'en_verse_text','he_verse_text','book_source','verses']
	list_display = ('question_text', 'verses','pub_date')
	inlines = [AnswerInline]
admin.site.register(Question, QuestionAdmin)


class SourceQuestionAdmin(admin.ModelAdmin):
	list_display = ['book_chapter_sentence']
admin.site.register(SourceQuestion, SourceQuestionAdmin)

class BookChapterQuestionsAdmin(admin.ModelAdmin):
	list_display = ('book_name', 'chapter', 'verses')
admin.site.register(BookChapterQuestions, BookChapterQuestionsAdmin)