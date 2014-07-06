from django.conf.urls import url, patterns

from goals import views

urlpatterns = patterns('',
  url(r'^$',views.index, name='index'),
  url(r'^(?P<goal_id>\d+)/$', views.detail, name='detail'),
)
