from django.contrib import admin
from qnotes.apps.quotes.models import Quote


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'note', 'user', 'source', 'is_private', 'created', 'modified',)
    list_display_links = ('quote',)

admin.site.register(Quote, QuoteAdmin)
