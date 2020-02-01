from django import forms


class UploadCVForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(max_length=100, required=True)
    phone = forms.CharField(max_length=20, required=True)
    cv_format = forms.ChoiceField(choices=[('', ''), ('modern_cv', 'Modern CV'), ('traditional_cv', 'Traditional CV')],
                                  required=True)
    cv_upload = forms.FileField(required=True)
    agree_to_terms = forms.BooleanField(required=True)

    # styling form widgets
    name.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'enter your name'})
    email.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'enter your email'})
    phone.widget.attrs.update({'class': 'form-control form-control-lg', 'placeholder': 'enter your phone number'})
    cv_format.widget.attrs.update({'class': 'form-control form-control-lg'})
    cv_upload.widget.attrs.update({'class': 'form-control form-control-lg'})
