# Generated by Django 3.0.3 on 2020-03-14 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0013_auto_20200313_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 13, 20, 33, 32, 493177)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='slug',
            field=models.CharField(default='myblog', max_length=200),
        ),
    ]
