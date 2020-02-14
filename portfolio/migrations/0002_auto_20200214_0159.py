# Generated by Django 2.2.7 on 2020-02-14 01:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailaction',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portfolio.Portfolio'),
        ),
        migrations.AlterField(
            model_name='emailaction',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 507451, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 504522, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='portfoliomailmessage',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 14, 1, 59, 50, 509403, tzinfo=utc)),
        ),
    ]
