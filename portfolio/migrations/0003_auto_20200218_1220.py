# Generated by Django 2.2.7 on 2020-02-18 12:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_auto_20200214_0159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 18, 12, 20, 40, 949809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 18, 12, 20, 40, 949809, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfoliomailmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 18, 12, 20, 40, 949809, tzinfo=utc)),
        ),
    ]
