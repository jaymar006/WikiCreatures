# Generated by Django 4.2.6 on 2024-01-27 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_fav_food_post_sci_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_discovered',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='discovered_by',
            new_name='location_discovered',
        ),
    ]
