# Generated by Django 2.2.7 on 2020-01-19 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0016_auto_20200119_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 20, 29, 27, 776401)),
        ),
    ]
