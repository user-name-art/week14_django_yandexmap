# Generated by Django 4.2.7 on 2023-12-12 18:58

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_alter_location_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.location', verbose_name='место'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='изображение'),
        ),
        migrations.AlterField(
            model_name='image',
            name='position',
            field=models.PositiveIntegerField(default=0, verbose_name='позиция'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description_long',
            field=tinymce.models.HTMLField(verbose_name='подробное описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description_short',
            field=models.TextField(verbose_name='короткое описание'),
        ),
        migrations.AlterField(
            model_name='location',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='название'),
        ),
    ]