from django.conf.urls import url

from poll import views

urlpatterns = [
    url(r'^vote/(?P<poll_pk>\d+)/$', views.vote, name='poll_ajax_vote'),
    url(r'^vote/(?P<poll_pk>\d+)/$', views.vote2, name='poll_ajax_vote2'),
    url(r'^poll/(?P<poll_pk>\d+)/$', views.poll, name='poll'),
    url(r'^result/$', views.result, name='poll_result'),
]
