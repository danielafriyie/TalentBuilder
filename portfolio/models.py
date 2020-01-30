from django.db import models
from django.utils.timezone import now


class TopAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/TopAd/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class BottomAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/BottomAd/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class RightAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/RightAd/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class LeftAd(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    image = models.ImageField(upload_to='BannerAds/Portfolio/LeftAd/%Y/%m/%d/')
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
    expiry = models.DateTimeField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    slug_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    p_headline = models.CharField(max_length=256)
    about = models.TextField()
    cv_upload = models.FileField(upload_to='Portfolio/CV/%Y/%m/%d/', blank=True)
    picture = models.ImageField(upload_to='Portfolio/picture/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=now())
    # Social Links
    facebook = models.URLField(max_length=255, blank=True)
    twitter = models.URLField(max_length=255, blank=True)
    instagram = models.URLField(max_length=255, blank=True)
    linkedin = models.URLField(max_length=255, blank=True)
    # Theme
    theme = models.CharField(max_length=20)
    # agree to terms
    agree_to_terms = models.CharField(max_length=10, default="false")
    # Portfolio link
    portfolio_link = models.CharField(max_length=255, blank=True)
    # Banner Ads
    banner_ad = models.ForeignKey(TopAd, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return self.name
