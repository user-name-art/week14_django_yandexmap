# Generated by Django 4.2.7 on 2023-12-19 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_location_long_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(upload_to='', verbose_name='изображение'),
        ),
    ]
