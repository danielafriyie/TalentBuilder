from django.db import models
from django.utils.timezone import now


class UploadCV(models.Model):
    name = models.CharField(max_length=255, blank=False)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    phone = models.CharField(max_length=20)
    career_type = models.CharField(max_length=255)
    cv_format = models.CharField(max_length=25, blank=False)
    cv_upload = models.FileField(upload_to='CV/%Y/%m/%d/', blank=False)
    agree_to_terms = models.BooleanField()
    revised_cv = models.FileField(upload_to='RevisedCV/%Y/%m/%d/', blank=True)
    date = models.DateTimeField(default=now())

    def __str__(self):
        return self.name
