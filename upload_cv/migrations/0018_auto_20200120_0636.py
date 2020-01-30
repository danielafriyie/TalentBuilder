# Generated by Django 2.2.7 on 2020-01-20 06:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('upload_cv', '0017_auto_20200119_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='BottomAd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='BannerAds/CV/BottomAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 6, 36, 58, 902019))),
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
                ('image', models.ImageField(upload_to='BannerAds/CV/LeftAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 6, 36, 58, 903019))),
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
                ('image', models.ImageField(upload_to='BannerAds/CV/RightAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 6, 36, 58, 903019))),
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
                ('image', models.ImageField(upload_to='BannerAds/CV/TopAd/%Y/%m/%d/')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 1, 20, 6, 36, 58, 901021, tzinfo=utc))),
                ('expiry', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 20, 6, 36, 58, 900022)),
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='uploadcv',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
