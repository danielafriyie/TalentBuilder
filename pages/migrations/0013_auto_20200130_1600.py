# Generated by Django 2.2.7 on 2020-01-30 16:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_auto_20200130_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerads',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 30, 16, 0, 40, 568761, tzinfo=utc)),
        ),
    ]