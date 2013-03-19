from django.contrib import admin
from .models import Quote, Note


class QuoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'user', 'source', 'privacy_state', 'created', 'modified',)
    list_display_links = ('quote',)
    prepopulated_fields = {'slug': ('quote',)}


class NoteAdmin(admin.ModelAdmin):
    list_display = ('quote', 'get_media_type_display', 'text_note', 'video_url', 'sound_url', 'created', 'modified',)
    list_display_links = ('get_media_type_display',)

admin.site.register(Quote, QuoteAdmin)
admin.site.register(Note, NoteAdmin)