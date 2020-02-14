# Generated by Django 2.2.7 on 2020-02-14 01:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0006_auto_20200214_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaction',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='upload_cv.UploadCV'),
        ),
        migrations.AlterField(
            model_name='emailaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 483044, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 482067, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='uploadcvmailmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 484997, tzinfo=utc)),
        ),
    ]
