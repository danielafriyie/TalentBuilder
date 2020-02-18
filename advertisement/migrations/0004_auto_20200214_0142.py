# Generated by Django 2.2.7 on 2020-02-14 01:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('advertisement', '0003_auto_20200214_0138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banneradrate',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 42, 16, 324764, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='bottomad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 42, 16, 326772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leftad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 42, 16, 329764, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolioad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 42, 16, 329764, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rightad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 42, 16, 327772, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 42, 16, 325771, tzinfo=utc)),
        ),
    ]