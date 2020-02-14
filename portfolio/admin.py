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


class EmailActionAdmin(admin.ModelAdmin):
    list_display = ('id', 'client_id', 'action', 'date')
    list_display_links = ('id', 'client_id')
    list_filter = ('action', 'date')
    search_fields = ('id', 'client_id', 'date')
    list_per_page = 25


admin.site.register(models.EmailAction, EmailActionAdmin)


class MailMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'host_user', 'subject', 'before_msg', 'after_msg', 'date')
    list_display_links = ('id', 'host_user')
    list_filter = ('date',)
    search_fields = ('id', 'host_user', 'date')
    list_per_page = 25


admin.site.register(models.PortfolioMailMessage, MailMessageAdmin)
