from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^api/saved_list$', 'base.views.saved_list_sync'),
    url(r'^api/saved_list/(?P<id>\d+)$', 'base.views.saved_list'),
    url(r'^api/question_map/$', 'base.views.question_map')
)