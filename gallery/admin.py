from django.contrib import admin
from unfold.admin import ModelAdmin

from gallery.models import Photograph


class PhotographModelAdmin(ModelAdmin):
    list_display = ('name', 'legend', 'published',)
    list_display_links = ('name', 'legend',)
    list_filter = ('category',)
    list_editable = ('published',)
    search_fields = ('name',)
    list_per_page = 100
    ordering = ('name',)
    search_help_text = 'earch by: name'


admin.site.register(Photograph, PhotographModelAdmin)
