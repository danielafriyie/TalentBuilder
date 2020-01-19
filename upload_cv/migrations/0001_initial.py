# Generated by Django 2.2.7 on 2019-12-23 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadCV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=256, unique=True)),
                ('cv_format', models.CharField(max_length=25)),
                ('cv_upload', models.FileField(upload_to='CV/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 12, 23, 21, 44, 43, 207835))),
            ],
        ),
    ]