# Generated by Django 2.2.7 on 2020-01-19 14:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerAds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('rate', models.FileField(upload_to='BannerAds/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 19, 14, 46, 57, 25286))),
            ],
        ),
    ]