# Generated by Django 2.2.7 on 2020-01-19 17:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerads',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 17, 44, 45, 622771)),
        ),
    ]
