# Generated by Django 2.2.7 on 2019-12-24 16:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0005_auto_20191224_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 16, 49, 12, 907229)),
        ),
    ]
