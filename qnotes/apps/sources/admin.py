from django.contrib import admin
from qnotes.apps.sources.models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'url', 'isbn')
    list_display_links = ('title',)
admin.site.register(Source, SourceAdmin)
