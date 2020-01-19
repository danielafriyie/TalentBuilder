from django.db import models
from datetime import datetime as dt


class UploadCV(models.Model):
    name = models.CharField(max_length=256, blank=False)
    email = models.EmailField(max_length=256, unique=True, blank=False)
    phone = models.CharField(max_length=20)
    cv_format = models.CharField(max_length=25, blank=False)
    cv_upload = models.FileField(upload_to='CV/%Y/%m/%d/', blank=False)
    agree_to_terms = models.CharField(max_length=10, default="false")
    revised_cv = models.FileField(upload_to='RevisedCV/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=dt.now())

    def __str__(self):
        return self.name
