# Generated by Django 2.2.7 on 2020-01-19 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0009_auto_20191225_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadcv',
            name='agree_to_terms',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 14, 10, 24, 517700)),
        ),
    ]
