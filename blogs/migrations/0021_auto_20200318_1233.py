# Generated by Django 3.0.3 on 2020-03-19 00:33

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogs', '0020_auto_20200318_1024'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 18, 12, 33, 7, 400588)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 18, 12, 33, 7, 399588)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='userid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
