# Generated by Django 3.2 on 2024-06-19 03:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20240619_1000'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='post',
            name='file',
        ),
    ]
