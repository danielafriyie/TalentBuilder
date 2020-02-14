# Generated by Django 2.2.7 on 2020-02-14 01:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('advertisement', '0006_auto_20200214_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='PortfolioMailMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('before_msg', models.CharField(max_length=255)),
                ('after_msg', models.CharField(max_length=255)),
                ('host_user', models.EmailField(max_length=255)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 50, 40, 490817, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('p_headline', models.CharField(max_length=256)),
                ('about', models.TextField()),
                ('cv_upload', models.FileField(blank=True, upload_to='Portfolio/CV/%Y/%m/%d/')),
                ('picture', models.ImageField(blank=True, upload_to='Portfolio/picture/%Y/%m/%d/')),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 50, 40, 487819, tzinfo=utc))),
                ('facebook', models.URLField(blank=True, max_length=255)),
                ('twitter', models.URLField(blank=True, max_length=255)),
                ('instagram', models.URLField(blank=True, max_length=255)),
                ('linkedin', models.URLField(blank=True, max_length=255)),
                ('theme', models.CharField(max_length=20)),
                ('agree_to_terms', models.CharField(default='false', max_length=10)),
                ('portfolio_link', models.CharField(blank=True, max_length=255)),
                ('banner_ad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='advertisement.PortfolioAd')),
            ],
        ),
        migrations.CreateModel(
            name='EmailAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(max_length=20)),
                ('date', models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 50, 40, 489818, tzinfo=utc))),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Portfolio')),
            ],
        ),
    ]
