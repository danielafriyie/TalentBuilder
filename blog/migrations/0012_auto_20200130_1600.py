# Generated by Django 2.2.7 on 2020-01-30 16:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200130_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 650557, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 651056, tzinfo=utc)),
        ),
    ]
