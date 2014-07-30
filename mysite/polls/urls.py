from django.conf.urls import patterns,include, url

from polls import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
   # url(r'^$', views.index, name='index'
   
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # url(r'^polls/', include('polls.urls')),
    #url(r'^admin/', include(admin.site.urls)),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
)
