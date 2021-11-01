# Generated by Django 3.2.6 on 2021-08-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_alter_mainbanner_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Имя')),
                ('img', models.ImageField(upload_to='media', verbose_name='Логотип')),
            ],
            options={
                'verbose_name': 'Партнёр',
                'verbose_name_plural': 'Партнёра',
            },
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='img',
            field=models.ImageField(upload_to='media', verbose_name='Баннер'),
        ),
    ]
