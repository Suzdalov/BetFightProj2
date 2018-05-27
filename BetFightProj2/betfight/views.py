from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.views.generic import ListView
from .models import match


class sheduleView(ListView):
        model=match
        template_name = 'shedule.html'
 


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'betfight/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def iifh2018(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'betfight/iihf2018.html',
        {
            'title':'World Championshop',
            'year':datetime.now().year,
        }
    )