# Generated by Django 3.2.6 on 2021-09-02 07:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0021_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.CharField(blank=True, default=uuid.uuid1, max_length=300, unique=True, verbose_name='URL (Необязательно)'),
        ),
    ]
