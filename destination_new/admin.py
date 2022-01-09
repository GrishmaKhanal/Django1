from django.contrib import admin
from django.contrib.admin.sites import site
from django.db.models.query_utils import RegisterLookupMixin
from .models import *


admin.site.register(destination)
admin.site.register(district)
admin.site.register(categories)
admin.site.register(new)
admin.site.register(airport)
