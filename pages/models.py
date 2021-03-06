from django.db import models
from django.utils.timezone import now


class Testimonials(models.Model):
    name = models.CharField(max_length=100)
    testimony = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.name


class ShortListCompanies(models.Model):
    name = models.CharField(max_length=100)
    logo_image = models.ImageField(upload_to='short_list/%Y/%m/%d/', blank=True, null=True)
    font_awesome_class = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.name

