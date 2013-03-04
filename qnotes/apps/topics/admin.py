from django.contrib import admin
from qnotes.apps.topics.models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Topic, TopicAdmin)
