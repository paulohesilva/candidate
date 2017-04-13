__author__ = 'paulo'

from django.conf.urls import url, patterns, include
from . import views

urlpatterns = patterns(
    '',
    url(r'^register-by-token/(?P<backend>[^/]+)/$', views.register_by_access_token),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)



