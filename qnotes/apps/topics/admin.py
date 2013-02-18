from django.contrib import admin
from qnotes.apps.topics.models import Topic


class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
admin.site.register(Topic, TopicAdmin)
