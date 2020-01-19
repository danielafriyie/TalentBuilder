from django.db import models
from datetime import datetime as dt


class Portfolio(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=20)
    p_headline = models.CharField(max_length=256)
    about = models.TextField()
    cv_upload = models.FileField(upload_to='Portfolio/CV/%Y/%m/%d/', blank=True)
    picture = models.ImageField(upload_to='Portfolio/picture/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=dt.now())
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

    def __str__(self):
        return self.name
