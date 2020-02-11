from django.db import models
from django.utils.timezone import now


class BannerAdRate(models.Model):
    title = models.CharField(max_length=255)
    rate = models.FileField(upload_to='BannerAds/%Y/%m/%d/')
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.title


class TopAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/TopAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BottomAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/BottomAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RightAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/RightAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LeftAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/LeftAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PortfolioAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='BannerAds/Portfolio/PortfolioAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
