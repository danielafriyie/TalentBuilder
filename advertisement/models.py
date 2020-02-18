from django.db import models
from django.utils.timezone import now


class BannerAdRate(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    rate = models.FileField(upload_to='BannerAds/%Y/%m/%d/', blank=True, null=True)
    html_tag = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.title


class TopAd(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='BannerAds/Portfolio/TopAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html_tag = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BottomAd(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='BannerAds/Portfolio/BottomAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html_tag = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RightAd(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='BannerAds/Portfolio/RightAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html_tag = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LeftAd(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='BannerAds/Portfolio/LeftAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html_tag = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class PortfolioAd(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='BannerAds/Portfolio/PortfolioAd/%Y/%m/%d/', blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    html_tag = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name
