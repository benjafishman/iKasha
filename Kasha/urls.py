from django.conf.urls import url

from . import views

app_name = 'kasha'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book>[a-zA-Z]+)/(?P<chapter>[0-9]+)/(?P<sentence>[0-9]+)/$', views.question_list, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/$', views.question_detail, name='question_detail'),
    url(r'^(?P<book>[a-zA-Z]+)/(?P<chapter>[0-9]+)/$', views.get_text, name='get_text	'),
]