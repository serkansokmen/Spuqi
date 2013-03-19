from django.contrib import admin
from .models import Collection


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'user')
    list_display_links = ('title',)
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Collection, CollectionAdmin)
