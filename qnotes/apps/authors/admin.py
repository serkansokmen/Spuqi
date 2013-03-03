from django.contrib import admin
from qnotes.apps.authors.models import Author


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
admin.site.register(Author, AuthorAdmin)
