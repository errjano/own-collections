# Generated by Django 4.0.6 on 2022-07-17 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_alter_category_item_type_alter_category_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='item_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', related_query_name='category', to='catalog.itemtype'),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='childs', related_query_name='child', to='catalog.category'),
        ),
    ]
