# Generated by Django 2.2.7 on 2020-01-26 15:25

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200120_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 26, 15, 25, 15, 528738, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 26, 15, 25, 15, 529238, tzinfo=utc)),
        ),
    ]
