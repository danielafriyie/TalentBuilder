# Generated by Django 2.2.7 on 2019-12-24 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('p_headline', models.CharField(max_length=256)),
                ('about', models.TextField()),
                ('cv_upload', models.FileField(blank=True, upload_to='Portfolio/CV/%Y/%m/%d/')),
                ('picture', models.ImageField(blank=True, upload_to='Portfolio/picture/%Y/%m/%d/')),
                ('facebook', models.URLField(blank=True, max_length=255)),
                ('twitter', models.URLField(blank=True, max_length=255)),
                ('instagram', models.URLField(blank=True, max_length=255)),
                ('linkedin', models.URLField(blank=True, max_length=255)),
                ('theme', models.CharField(max_length=20)),
            ],
        ),
    ]