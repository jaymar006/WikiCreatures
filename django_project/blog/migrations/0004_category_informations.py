# Generated by Django 4.2.6 on 2024-01-28 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_date_discovered_post_location_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_informations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories_type', models.CharField(max_length=255)),
                ('categories_description', models.TextField()),
                ('category_image', models.ImageField(upload_to='category_images/%Y')),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='category_images/catview_images/%Y')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='category_images/catview_images/%Y')),
                ('image_three', models.ImageField(blank=True, null=True, upload_to='category_images/catview_images/%Y')),
                ('image_four', models.ImageField(blank=True, null=True, upload_to='category_images/catview_images/%Y')),
                ('image_five', models.ImageField(blank=True, null=True, upload_to='category_images/catview_images/%Y')),
                ('image_six', models.ImageField(blank=True, null=True, upload_to='category_images/catview_images/%Y')),
                ('characteristics', models.TextField()),
                ('habitat', models.TextField()),
                ('diet', models.TextField()),
                ('reproduction', models.TextField()),
                ('notable_species', models.TextField()),
            ],
        ),
    ]
