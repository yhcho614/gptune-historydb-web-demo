from django.contrib import admin

# Register your models here.

from .models import PerfFile

admin.site.register(PerfFile)
