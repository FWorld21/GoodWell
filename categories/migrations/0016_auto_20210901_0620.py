# Generated by Django 3.2.6 on 2021-09-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0015_auto_20210901_0620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flameretard',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='flameretard',
            name='price',
            field=models.CharField(max_length=100, verbose_name='Цена'),
        ),
    ]
