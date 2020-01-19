from django.contrib import admin
from . import models


class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'slug_field', 'date')
    list_display_links = ('id', 'author')
    list_editable = ('title', 'slug_field')
    list_filter = ('date',)
    search_fields = ('id', 'title', 'date')
    list_per_page = 25


admin.site.register(models.Blog, BlogAdmin)