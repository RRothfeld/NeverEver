from django.conf.urls import patterns, url
from NHIE import views

urlpatterns = patterns(
		url(r'', views.index, name='index'),
        url(r'index', views.index, name='index'),
        url(r'about', views.about, name='about'))
