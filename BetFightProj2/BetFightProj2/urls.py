"""
Definition of urls for Beta_proj.
"""
import django.contrib.auth.views
from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#import betfight.forms
import betfight.views


urlpatterns = [
    # Examples:
    # url(r'^$', Beta_proj.views.home, name='home'),
    # url(r'^Beta_proj/', include('Beta_proj.Beta_proj.urls')),

    url(r'^$', betfight.views.home, name='home'),
 
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^iihf2018/', include('betfight.urls')),
]
