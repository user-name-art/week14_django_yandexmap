from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Location, Image
from adminsortable2.admin import SortableAdminBase, SortableStackedInline, SortableAdminMixin


class ImageInline(SortableStackedInline):
    extra = 1
    model = Image
    readonly_fields = ('get_preview',)
    fields = ('photo', 'get_preview', 'position')

    def get_preview(self, obj):
        return mark_safe('<img src="{url}" height={height} />'.format(
                url = obj.photo.url,
                height=200,
                )
        )


@admin.register(Location)
class LocationAdmin(SortableAdminBase, admin.ModelAdmin):
    inlines = [ImageInline]


admin.site.register(Image)
