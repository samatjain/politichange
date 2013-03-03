from django.conf.urls import patterns, include, url

from mauve_duck.agile_otter import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mauve_duck.views.home', name='home'),
    # url(r'^mauve_duck/', include('mauve_duck.foo.urls')),
    url(r'^$', views.index, name='index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^browserid/', include('django_browserid.urls')),

 	 url(r'^campaign$', views.registration, name='register'),

 	 url(r'^participants$', views.participants_list, name='register'),
 	 url(r'^participants/profile-female$', views.participant_profile, name='profile'),

 	 url(r'^politician$', views.politician_start, name='politician_start'),
 	 url(r'^politician/create-campaign', views.start_campaign, name='campaign_start'),
 	 url(r'^politician/campaign', views.campaign, name='campaign'),
)
