# Generated by Django 3.2.7 on 2021-11-25 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_fiiles_imagelibrary_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagelibrary',
            name='files',
        ),
    ]
