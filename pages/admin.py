from django.contrib import admin
from . import models


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    list_per_page = 25


admin.site.register(models.Testimonials, TestimonialAdmin)


class ShortListCompaniesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date')
    list_display_links = ('id', 'name')
    list_per_page = 25


admin.site.register(models.ShortListCompanies, ShortListCompaniesAdmin)

