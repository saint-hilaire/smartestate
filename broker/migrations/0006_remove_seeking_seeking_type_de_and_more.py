# Generated by Django 4.0 on 2022-09-24 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broker', '0005_matching_note_de_matching_note_en_matching_note_es_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seeking',
            name='seeking_type_de',
        ),
        migrations.RemoveField(
            model_name='seeking',
            name='seeking_type_en',
        ),
        migrations.RemoveField(
            model_name='seeking',
            name='seeking_type_es',
        ),
        migrations.RemoveField(
            model_name='seeking',
            name='seeking_type_fr',
        ),
        migrations.RemoveField(
            model_name='seeking',
            name='seeking_type_it',
        ),
    ]
