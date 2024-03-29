# Generated by Django 2.0.7 on 2021-04-08 05:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20210330_0507'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.TextField(default='user123', editable=False)),
                ('receiver', models.TextField(default='user123', editable=False)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2021, 4, 8, 10, 59, 44, 93203), verbose_name='Date Published')),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='tutorialseries',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 10, 59, 44, 87208), verbose_name='Date Published'),
        ),
    ]
