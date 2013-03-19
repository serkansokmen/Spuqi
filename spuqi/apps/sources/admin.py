from django.contrib import admin
from .models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'url', 'isbn', )
    list_display_links = ('title', )
    search_fields = ('title', 'url', 'isbn', )
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Source, SourceAdmin)
