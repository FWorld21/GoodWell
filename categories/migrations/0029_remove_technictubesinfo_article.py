# Generated by Django 3.2.6 on 2021-09-02 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0028_auto_20210902_1023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='technictubesinfo',
            name='article',
        ),
    ]
