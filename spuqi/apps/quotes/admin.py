from django.contrib import admin
from .models import Quote, Note
from imperavi.admin import ImperaviAdmin, ImperaviStackedInlineAdmin


class NoteInline(ImperaviStackedInlineAdmin):
    model = Note
    extra = 1
    unique_media = True
    #list_display = ('get_media_type_display', 'quote', 'text_note', 'video_url', 'sound_url', 'created', 'modified',)
    #list_display_links = ('get_media_type_display',)


class QuoteAdmin(ImperaviAdmin):
    list_display = ('quote', 'user', 'source', 'privacy_state', 'created', 'modified',)
    list_display_links = ('quote',)
    prepopulated_fields = {'slug': ('quote',)}
    inlines = [NoteInline]
    unique_media = True


admin.site.register(Quote, QuoteAdmin)
