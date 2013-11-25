
from django.conf.urls.defaults import *

from django.conf import settings


urlpatterns = patterns('data_demo',
  url(r'^$', 'views.index'),
  url(r'^index/$', 'views.index'),
  url (r'^data_upload/$', 'views.data_upload'),
  url (r'^choose_viz/$', 'views.choose_viz'), 
  url (r'^visualization/$', 'views.visualization'),
)


