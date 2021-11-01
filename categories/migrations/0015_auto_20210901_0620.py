# Generated by Django 3.2.6 on 2021-09-01 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0014_auto_20210901_0620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technicinfo',
            name='img',
        ),
        migrations.RemoveField(
            model_name='technicinfo',
            name='price',
        ),
        migrations.AddField(
            model_name='flameretard',
            name='img',
            field=models.ImageField(default='', upload_to='media', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='flameretard',
            name='price',
            field=models.CharField(default='', max_length=100, verbose_name='Цена'),
        ),
    ]
