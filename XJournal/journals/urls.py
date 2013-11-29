from django.conf.urls import patterns, url

from journals import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
#     url(r'^(?P<journal_id>\d+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<journal_id>\d+)/edit/$', views.edit, name='edit')
)

