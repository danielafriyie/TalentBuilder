# Generated by Django 2.2.7 on 2019-12-25 11:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfolio',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 25, 11, 49, 57, 403209)),
        ),
        migrations.AlterField(
            model_name='portfolio',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
