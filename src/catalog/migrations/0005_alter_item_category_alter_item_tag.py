# Generated by Django 4.0.6 on 2022-07-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_item_category_alter_item_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ManyToManyField(blank=True, related_name='items', related_query_name='item', to='catalog.category'),
        ),
        migrations.AlterField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='items', related_query_name='item', to='catalog.tag'),
        ),
    ]
