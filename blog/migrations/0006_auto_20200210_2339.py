# Generated by Django 2.2.7 on 2020-02-10 23:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200210_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 10, 23, 39, 24, 896578, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 10, 23, 39, 24, 897578, tzinfo=utc)),
        ),
    ]
