from django import forms
from datetime import datetime as dt


class UploadCV(forms.Form):
    name = forms.CharField(max_length=256)
    email = forms.EmailField(max_length=256)
    cv_upload = forms.FileField()
    date = forms.DateTimeField()
