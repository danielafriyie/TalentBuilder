# Generated by Django 2.2.7 on 2020-01-20 09:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0018_auto_20200120_0636'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottomAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='BannerAds/Portfolio/BottomAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 9, 56, 14, 142675, tzinfo=utc))),
                ('expiry', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LeftAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='BannerAds/Portfolio/LeftAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 9, 56, 14, 143674, tzinfo=utc))),
                ('expiry', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RightAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='BannerAds/Portfolio/RightAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 9, 56, 14, 143674, tzinfo=utc))),
                ('expiry', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TopAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='BannerAds/Portfolio/TopAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 9, 56, 14, 141676, tzinfo=utc))),
                ('expiry', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 20, 9, 56, 14, 140676, tzinfo=utc)),
        ),
    ]
