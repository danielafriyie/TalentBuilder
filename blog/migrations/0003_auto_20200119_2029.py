# Generated by Django 2.2.7 on 2020-01-19 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200119_1814'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug_field',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 20, 29, 27, 781393)),
        ),
    ]
