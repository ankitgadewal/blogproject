# Generated by Django 3.0.3 on 2020-03-15 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0016_auto_20200315_1155'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewBlog',
        ),
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 15, 11, 57, 10, 444888)),
        ),
    ]