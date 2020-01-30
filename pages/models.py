from django.db import models
from django.utils.timezone import now


class BannerAds(models.Model):
    title = models.CharField(max_length=255)
    rate = models.FileField(upload_to='BannerAds/%Y/%m/%d/')
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.title
