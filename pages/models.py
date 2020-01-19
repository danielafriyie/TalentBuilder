from django.db import models
from datetime import datetime as dt


class BannerAds(models.Model):
    title = models.CharField(max_length=255)
    rate = models.FileField(upload_to='BannerAds/%Y/%m/%d/')
    date = models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.title
