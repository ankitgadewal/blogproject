# Generated by Django 3.0.3 on 2020-03-08 00:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200306_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogs',
            name='image',
        ),
        migrations.AddField(
            model_name='blogs',
            name='slug',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 7, 12, 21, 24, 292379)),
        ),
    ]
