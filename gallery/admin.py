from django.contrib import admin

from gallery.models import Photograph


class PhotographModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'legend',)
    list_display_links = ('name', 'legend',)
    search_fields = ('name',)
    list_per_page = 100
    ordering = ('name',)
    search_help_text = 'earch by: name'


admin.site.register(Photograph, PhotographModelAdmin)
