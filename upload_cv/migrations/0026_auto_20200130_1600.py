# Generated by Django 2.2.7 on 2020-01-30 16:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0025_auto_20200130_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bottomad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 640576, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='leftad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 642073, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='rightad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 641574, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 640077, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 639578, tzinfo=utc)),
        ),
    ]
