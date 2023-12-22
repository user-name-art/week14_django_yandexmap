from adminsortable2.admin import (SortableAdminBase, SortableStackedInline)
from django.contrib import admin
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Image, Location


class ImageInline(SortableStackedInline):
    extra = 1
    model = Image
    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'position')

    def get_preview(self, image):
        max_height = 200
        max_width = 500
        return format_html(
            '<img src="{}" style="max-height:{}px;max-width:{}px;"/>',
            mark_safe(image.photo.url), max_height, max_width
            )


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    raw_id_fields = ('location',)
