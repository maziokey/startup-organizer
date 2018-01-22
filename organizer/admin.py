from django.contrib import admin

from .models import NewsLink, Startup, Tag

# Register your models here.
admin.site.register(NewsLink)
admin.site.register(Startup)
admin.site.register(Tag)
