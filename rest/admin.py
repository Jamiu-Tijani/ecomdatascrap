from django.contrib import admin

# Register your models here.
from .models import data


class FeedItemAdmin(admin.ModelAdmin): 
    list_display = ('id', 'title', 'url')

admin.site.register(data, FeedItemAdmin)