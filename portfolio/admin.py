from django.contrib import admin
from . import models


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'date', 'theme', 'agree_to_terms', 'banner_ad')
    list_display_links = ('id', 'name', 'email')
    list_editable = ('banner_ad',)
    list_filter = ('date', 'theme', 'agree_to_terms')
    search_fields = ('name', 'email', 'phone', 'date', 'theme')
    list_per_page = 25


admin.site.register(models.Portfolio, PortfolioAdmin)


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
