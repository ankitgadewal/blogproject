# Generated by Django 3.0.3 on 2020-03-14 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_auto_20200313_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 13, 18, 20, 22, 401925)),
        ),
    ]
