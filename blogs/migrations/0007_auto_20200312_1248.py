# Generated by Django 3.0.3 on 2020-03-13 00:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_auto_20200311_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 12, 12, 48, 49, 923495)),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='blogs',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]