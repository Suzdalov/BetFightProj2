from django.conf.urls import include, url

from .views import sheduleView
from . import views




urlpatterns = [
 url(r'^$', views.iifh2018, name='home'),
 url(r'^shedule/', sheduleView.as_view(), name='shedule'),
 ]