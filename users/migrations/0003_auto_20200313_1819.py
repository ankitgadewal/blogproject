# Generated by Django 3.0.3 on 2020-03-14 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200306_2053'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='password2',
            field=models.CharField(default='temp', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='users',
            name='username',
            field=models.CharField(default='username', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
