from django.conf.urls import patterns, url
from neverever import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'play/summary/', views.play_summary, name='play_summary'),
                       url(r'play/options/', views.play_options, name='play_options'),
                       url(r'play/$', views.play, name='play'),
                       url(r'new-statement', views.new_statement, name='new_statement'),
                       url(r'stats/?$', views.stats, name='stats'),
                       url(r'^about/', views.about, name='about'),
                       url(r'^add_player/$', views.add_player, name='add_player'),
                       url(r'^update_count/$', views.update_count, name='update_count'),
                       url(r'^like_statement/$', views.like_statement, name='like_statement'),
                       url(r'^set_name/$', views.set_name, name='set_name'),
)