from django.conf.urls import patterns, url

from journals import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<journal_id>\d+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new')
)

