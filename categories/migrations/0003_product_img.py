# Generated by Django 3.2.6 on 2021-08-31 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(default='', upload_to='media', verbose_name='Картинка'),
        ),
    ]
