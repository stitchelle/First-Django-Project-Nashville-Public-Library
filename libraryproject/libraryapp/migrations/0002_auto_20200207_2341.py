# Generated by Django 3.0.3 on 2020-02-07 23:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libraryapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='yearpublished',
            new_name='year_published',
        ),
    ]
