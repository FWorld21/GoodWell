# Generated by Django 3.2.6 on 2021-09-03 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0029_remove_technictubesinfo_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fitting',
            name='price',
        ),
        migrations.RemoveField(
            model_name='fitting',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='tubes',
            name='price',
        ),
        migrations.RemoveField(
            model_name='tubes',
            name='slug',
        ),
        migrations.DeleteModel(
            name='TechnicTubesInfo',
        ),
    ]
