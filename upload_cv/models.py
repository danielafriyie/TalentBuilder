from django.db import models
from django.utils.timezone import now
# from pages.models import MyEmailConfiguration


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


class EmailAction(models.Model):
    client_id = models.ForeignKey(UploadCV, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=20)
    date = models.DateTimeField(default=now())


class UploadCVMailMessage(models.Model):
    subject = models.CharField(max_length=255)
    before_msg = models.CharField(max_length=255)
    after_msg = models.CharField(max_length=255)
    host_user = models.CharField(max_length=255)
    date = models.DateTimeField(default=now())
