from django.contrib import admin
from django import forms
from flat_json_widget.widgets import FlatJsonWidget

from catalog.models import ItemType, Item, Category, Tag


class MetadataJsonForm(forms.ModelForm):
    class Meta:
        widgets = {
            "metadata" : FlatJsonWidget
        }

class SluggedModel(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class ItemAdmin(admin.ModelAdmin):
    list_display = ["__str__", "humanized_metadata",]
    list_filter = ["category", "item_type", "tag",]
    filter_horizontal = ["category", "tag",]
    form = MetadataJsonForm


class CategoryAdmin(SluggedModel):
    list_display = ["slug", "title", "item_type", "parent",]
    list_filter = ["parent", "item_type",]
    list_editable = ["title",]

class TagAdmin(SluggedModel):
    list_display = ["slug", "title", "description",]
    list_editable = ["title",]



admin.site.register(ItemType, SluggedModel)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Item, ItemAdmin)