from django.contrib import admin
from . import models


class UploadCVAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'date', 'cv_format', 'agree_to_terms', 'revised_cv')
    list_display_links = ('id', 'name', 'email')
    list_editable = ('revised_cv',)
    list_filter = ('cv_format', 'date', 'agree_to_terms')
    search_fields = ('name', 'email', 'cv_format', 'date', 'phone')
    list_per_page = 25


admin.site.register(models.UploadCV, UploadCVAdmin)


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
