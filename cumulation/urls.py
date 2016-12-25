from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^countries/$', views.country_list, name='country_list'),
    url(r'^new/$', views.country_new, name='country_new'),
    url(r'^countries/(?P<country_id>[0-9]+)/$', views.detail, name='detail'),
]