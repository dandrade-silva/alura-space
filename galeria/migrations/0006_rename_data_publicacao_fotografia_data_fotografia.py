# Generated by Django 4.2.2 on 2023-06-28 22:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_fotografia_data_publicacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fotografia',
            old_name='data_publicacao',
            new_name='data_fotografia',
        ),
    ]