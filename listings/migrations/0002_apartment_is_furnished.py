# Generated by Django 4.0.1 on 2022-06-04 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartment',
            name='is_furnished',
            field=models.BooleanField(default=False),
        ),
    ]
