# Generated by Django 4.0 on 2022-09-24 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_apartment_flooring_de_apartment_flooring_en_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='listing_type_de',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='listing_type_en',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='listing_type_es',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='listing_type_fr',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='listing_type_it',
        ),
    ]
