from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'lists.views.home_page', name='home'),
    url(r'^polls/', include('polls.urls', namespace = 'polls')),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^lists/', include('lists.urls')),
)
