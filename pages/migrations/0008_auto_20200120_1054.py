# Generated by Django 2.2.7 on 2020-01-20 10:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200120_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerads',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 20, 10, 54, 49, 676521, tzinfo=utc)),
        ),
    ]