# Generated by Django 3.2.6 on 2021-08-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_metatags_title_uz'),
    ]

    operations = [
        migrations.AlterField(
            model_name='metatags',
            name='title_uz',
            field=models.CharField(max_length=300, verbose_name='Title (УЗБ)'),
        ),
    ]
