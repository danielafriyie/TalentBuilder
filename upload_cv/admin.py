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
