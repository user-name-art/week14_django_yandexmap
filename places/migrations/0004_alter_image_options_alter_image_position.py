# Generated by Django 4.2.7 on 2023-11-24 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
