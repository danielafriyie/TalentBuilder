# Generated by Django 2.2.7 on 2020-02-14 01:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0005_auto_20200214_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 50, 40, 477825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 50, 40, 476825, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadcvmailmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 50, 40, 478824, tzinfo=utc)),
        ),
    ]