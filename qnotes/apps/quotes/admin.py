from django.contrib import admin
from qnotes.apps.quotes.models import Quote, Note


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'user', 'source', 'is_private', 'created', 'modified',)
    list_display_links = ('quote',)
    filter_horizontal = ['topics', ]


class NoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'get_media_type_display', 'text_note', 'video_url', 'sound_url', 'created', 'modified',)
    list_display_links = ('get_media_type_display',)

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Note, NoteAdmin)
