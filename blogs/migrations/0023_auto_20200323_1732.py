# Generated by Django 3.0.3 on 2020-03-24 05:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0022_auto_20200323_1730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 23, 17, 32, 26, 167790)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(default='Desert.jpg', upload_to=''),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 23, 17, 32, 26, 167790)),
        ),
    ]
