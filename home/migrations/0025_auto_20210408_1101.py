# Generated by Django 2.0.7 on 2021-04-08 05:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_auto_20210408_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 11, 1, 37, 457632), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 11, 1, 37, 453634), verbose_name='Date Published'),
        ),
    ]
