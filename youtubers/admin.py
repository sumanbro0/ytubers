from django.contrib import admin
from .models import Youtuber
from django.utils.html import format_html
# Register your models here.


class ytAdmin(admin.ModelAdmin):

    def myphoto(self, object):
        return format_html('<img src="{}" width="40px" />'.format(object.photo.url))

    list_display = ('id', 'myphoto', 'name', 'subs_count', 'is_featured')
    list_display_links = ('name', 'id')
    search_fields = ('name', 'subs_count')
    list_filter = ('camera_type', 'category')
    list_editable = ('is_featured',)


admin.site.register(Youtuber, ytAdmin)
