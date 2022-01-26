# Generated by Django 2.0.7 on 2020-07-01 22:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=45)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 7, 2, 3, 36, 10, 854010), verbose_name='Date Published')),
                ('content', models.TextField()),
            ],
        ),
    ]