from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'krossover.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^coaches/', include('coaches.urls', namespace='coaches')),
    url(r'^admin/', include(admin.site.urls)),
)
