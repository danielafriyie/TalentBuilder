from django.db import models
from django.utils.timezone import now


class Blog(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug_field = models.CharField(max_length=255)
    summary = models.TextField(max_length=255)
    meta_content = models.TextField(max_length=255)
    image = models.ImageField(upload_to='Blog/%Y/%m/%d/')
    body = models.TextField()
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.title


class TopAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Blog/TopAd/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
