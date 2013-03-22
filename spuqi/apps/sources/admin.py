from django.contrib import admin
from .models import Source


class SourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'web_address', 'isbn', )
    list_display_links = ('title', )
    search_fields = ('title', 'web_address', 'isbn', )
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Source, SourceAdmin)
