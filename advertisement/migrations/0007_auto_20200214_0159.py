# Generated by Django 2.2.7 on 2020-02-14 01:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0006_auto_20200214_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneradrate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 490855, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bottomad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 494759, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leftad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 500617, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolioad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 502572, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rightad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 496712, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 492807, tzinfo=utc)),
        ),
    ]