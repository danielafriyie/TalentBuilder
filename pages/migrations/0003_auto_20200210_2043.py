# Generated by Django 2.2.7 on 2020-02-10 20:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200210_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 10, 20, 43, 12, 642716, tzinfo=utc)),
        ),
    ]
