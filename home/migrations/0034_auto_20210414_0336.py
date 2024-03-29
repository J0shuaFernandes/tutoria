# Generated by Django 2.0.7 on 2021-04-13 22:06

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20210413_2131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 3, 36, 14, 202479), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 14, 3, 36, 14, 197484), verbose_name='Date Published'),
        ),
    ]
