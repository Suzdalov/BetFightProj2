from django.contrib import admin
from .models import event
from .models import team
from .models import match

admin.site.register(event)
admin.site.register(team)
admin.site.register(match)