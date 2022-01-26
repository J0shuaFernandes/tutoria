# Generated by Django 2.0.7 on 2021-04-14 22:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0039_auto_20210415_0345'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='author',
        ),
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 3, 47, 18, 346170), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 3, 47, 18, 342175), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 15, 3, 47, 18, 339178), verbose_name='Date Published'),
        ),
    ]
