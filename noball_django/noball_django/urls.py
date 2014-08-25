from django.conf.urls import patterns, include, url

from django.contrib import admin
from noball_django.settings import DEBUG, STATIC_ROOT


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'
    ,{'document_root': STATIC_ROOT}),
    url(r'^mlb/', include('mlb.urls')),
)
