# Generated by Django 2.0.7 on 2021-03-29 23:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20210330_0459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorialseries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 30, 5, 7, 38, 75863), verbose_name='Date Published'),
        ),
    ]
