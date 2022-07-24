from django.contrib import admin
from django.db import models
from django.utils.html import format_html


class ItemType(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Tipo de item"
        verbose_name_plural = "Tipos de Item"


class Tag(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400, blank=True, null=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Etiqueta"
        verbose_name_plural = "Etiquetas"


class Category(models.Model):
    slug = models.SlugField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400, blank=True, null=True)
    parent = models.ForeignKey(
        "self", blank=True, null=True, on_delete=models.SET_NULL,
        related_name="childs", related_query_name="child")
    item_type = models.ForeignKey(
        "ItemType", null=True, on_delete=models.SET_NULL,
        related_name="categories", related_query_name="category")

    def __str__(self):
        return f"{self.item_type.title} - {self.title}"

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class Item(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=400, blank=True, null=True)
    item_type = models.ForeignKey(
        "ItemType", null=True, on_delete=models.SET_NULL,
        related_name="items", related_query_name="item")
    category = models.ManyToManyField(
        "Category", blank=True, related_name="items", related_query_name="item")
    tag = models.ManyToManyField(
        "Tag", blank=True, related_name="items", related_query_name="item")
    metadata = models.JSONField()

    def __str__(self):
        return f"{self.item_type.title} - {self.title}"

    @admin.display
    def humanized_metadata(self):
        op = []
        try:
            for key,value in self.metadata.items():
                op.append(f"<li>{key}: {value}</li>")
            return format_html(f"<ul>{''.join(op)}</ul>")
        except Exception:
            pass
        return ""

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
