# Generated by Django 4.2.7 on 2023-12-19 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_alter_image_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(db_index=True, default=0, verbose_name='позиция'),
        ),
    ]
