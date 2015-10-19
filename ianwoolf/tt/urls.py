from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from tt import views

urlpatterns = [
    url(r'^2people/$', views.PeopleList2.as_view()),
    url(r'^2people/(?P<pk>[0-9]+)/$', views.PeopleDetail2.as_view()),
    url(r'^3people/$', views.PeopleList3.as_view()),
    url(r'^3people/(?P<pk>[0-9]+)/$', views.PeopleDetail3.as_view()),
    url(r'^dbmv/$', views.DBMVList3.as_view()),
    url(r'^dbmv/(?P<pk>[0-9]+)/$', views.DBMVDetail3.as_view()),
    url(r'^my/$', 'tt.views.myown'),
    url(r'^my2/$', 'tt.views.myown2'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
