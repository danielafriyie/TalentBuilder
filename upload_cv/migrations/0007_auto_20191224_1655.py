# Generated by Django 2.2.7 on 2019-12-24 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0006_auto_20191224_1649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 16, 55, 53, 991476)),
        ),
    ]
