# Generated by Django 2.2.7 on 2019-12-24 14:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0002_auto_20191223_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadcv',
            name='phone',
            field=models.IntegerField(default=2019, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 24, 14, 36, 5, 992100)),
        ),
    ]