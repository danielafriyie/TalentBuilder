from django.db import models
from datetime import datetime as dt


class Blog(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    slug_field = models.CharField(max_length=255)
    summary = models.TextField(max_length=255)
    meta_content = models.TextField(max_length=255)
    image = models.ImageField(upload_to='Blog/%Y/%m/%d/')
    body = models.TextField()
    date = models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.title
