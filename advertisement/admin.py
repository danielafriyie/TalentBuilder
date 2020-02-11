from django.contrib import admin
from . import models


class TopAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'date', 'expiry', 'status')
    list_display_links = ('id', 'name', 'title')
    list_editable = ('expiry', 'status')
    list_filter = ('date', 'status')
    search_fields = ('id', 'name', 'title')
    list_per_page = 25


admin.site.register(models.TopAd, TopAdAdmin)


class BottomAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'date', 'expiry', 'status')
    list_display_links = ('id', 'name', 'title')
    list_editable = ('expiry', 'status')
    list_filter = ('date', 'status')
    search_fields = ('id', 'name', 'title')
    list_per_page = 25


admin.site.register(models.BottomAd, BottomAdAdmin)


class RightAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'date', 'expiry', 'status')
    list_display_links = ('id', 'name', 'title')
    list_editable = ('expiry', 'status')
    list_filter = ('date', 'status')
    search_fields = ('id', 'name', 'title')
    list_per_page = 25


admin.site.register(models.RightAd, RightAdAdmin)


class LeftAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'date', 'expiry', 'status')
    list_display_links = ('id', 'name', 'title')
    list_editable = ('expiry', 'status')
    list_filter = ('date', 'status')
    search_fields = ('id', 'name', 'title')
    list_per_page = 25


admin.site.register(models.LeftAd, LeftAdAdmin)


class PortfolioAdAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'title', 'date', 'expiry', 'status')
    list_display_links = ('id', 'name', 'title')
    list_editable = ('expiry', 'status')
    list_filter = ('date', 'status')
    search_fields = ('id', 'name', 'title')
    list_per_page = 25


admin.site.register(models.PortfolioAd, PortfolioAdAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = ('id', 'title')
    list_per_page = 25


admin.site.register(models.BannerAdRate, BannerAdmin)
