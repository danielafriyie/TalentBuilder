from django.contrib import admin
from . import models


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(models.BannerAds, BannerAdmin)
