# Generated by Django 2.0 on 2018-03-27 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20180327_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='title',
            new_name='producto',
        ),
    ]
