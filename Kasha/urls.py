from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<book>[a-zA-Z]+)/(?P<chapter>[0-9]+)/(?P<sentence>[0-9]+)/$', views.question_list, name='detail'),
]