from django.conf.urls import url, patterns

from coaches import views

urlpatterns = patterns('',
  url(r'^$',views.index, name='index'),
  url(r'^(?P<coach_id>\d+)/$', views.detail, name='detail'),
)
