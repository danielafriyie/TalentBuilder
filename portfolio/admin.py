from django.contrib import admin
from . import models


class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone', 'date', 'theme', 'agree_to_terms', 'portfolio_link')
    list_display_links = ('id', 'name', 'email')
    list_editable = ('portfolio_link',)
    list_filter = ('date', 'theme', 'agree_to_terms')
    search_fields = ('name', 'email', 'phone', 'date', 'theme')
    list_per_page = 25


admin.site.register(models.Portfolio, PortfolioAdmin)
