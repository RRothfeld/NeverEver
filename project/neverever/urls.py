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
                       #TODO:Remove
                       url(r'^testing/category/(?P<category_name_slug>[\w\-]+)/$', views.testing_category,
                           name='testing_category'),
                       url(r'^testing/?$', views.testing, name='testing'),
                       url(r'^add_player/$', views.add_player, name='add_player'),
                       url(r'^like_statement/$', views.like_statement, name='like_statement'),

)