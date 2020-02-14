from django.contrib import admin
from . import models


class UploadCVAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'cv_format', 'career_type', 'agree_to_terms', 'revised_cv')
    list_display_links = ('id', 'name', 'email')
    list_editable = ('revised_cv',)
    list_filter = ('cv_format', 'date', 'agree_to_terms')
    search_fields = ('name', 'email', 'cv_format', 'date', 'phone')
    list_per_page = 25


admin.site.register(models.UploadCV, UploadCVAdmin)


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

admin.site.register(models.UploadCVMailMessage, MailMessageAdmin)
