from django.db import models
from django.utils.timezone import now
from advertisement.models import PortfolioAd


# from pages.models import MyEmailConfiguration


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
    banner_ad = models.ForeignKey(PortfolioAd, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.id}.{self.slug_name}'


class EmailAction(models.Model):
    client_id = models.ForeignKey(Portfolio, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20)
    date = models.DateTimeField(default=now())


class PortfolioMailMessage(models.Model):
    subject = models.CharField(max_length=255)
    before_msg = models.CharField(max_length=255)
    after_msg = models.CharField(max_length=255)
    host_user = models.EmailField(max_length=255)
    date = models.DateTimeField(default=now())
