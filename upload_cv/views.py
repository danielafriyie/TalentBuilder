from django.shortcuts import render, redirect
from django.contrib import messages as msg
from django.views.generic import View
from . import models
from . import forms


# Function base view
def upload_cv(request):
    # Forms
    upload_cv_form = forms.UploadCVForm()
    # Advertisements
    top_ad = models.TopAd.objects.filter(status=True).all().first()
    bottom_ad = models.BottomAd.objects.all().filter(status=True)
    left_ad = models.LeftAd.objects.all().filter(status=True).first()
    right_ad = models.RightAd.objects.all().filter(status=True).first()
    context = {
        'topAd': top_ad,
        'bottomAd': bottom_ad,
        'leftAd': left_ad,
        'rightAd': right_ad,
        'upload_cv_form': upload_cv_form
    }
    # check if it's a post request
    if request.method == 'POST':

        # check if form is valid
        if upload_cv_form.is_valid():

            # get form data
            name = upload_cv_form.cleaned_data['name']
            email = upload_cv_form.cleaned_data['email']
            phone = upload_cv_form.cleaned_data['phone']
            cv_format = upload_cv_form.cleaned_data['cv_format']
            cv_upload = upload_cv_form.cleaned_data['cv_upload']

            # check if email exists
            if models.UploadCV.objects.filter(email=email).exists():
                msg.error(request, 'Email already exists!')
                return redirect('upload_cv')
            else:
                # insert data to database
                data = models.UploadCV.objects.create(
                    name=name, email=email, phone=phone, cv_format=cv_format, cv_upload=cv_upload
                )
                data.save()
                msg.success(request, 'Uploaded Successfully')
                return redirect('cv_appreciation')

        else:
            msg.error(request, 'Invalid data')
            return redirect('upload_cv')

    return render(request, 'upload_cv/upload_cv.html', context)


# Class Base View
class UploadCVView(View):

    def get(self, request):
        # Forms
        upload_cv_form = forms.UploadCVForm()
        # Advertisements
        top_ad = models.TopAd.objects.filter(status=True).all().first()
        bottom_ad = models.BottomAd.objects.all().filter(status=True)
        left_ad = models.LeftAd.objects.all().filter(status=True).first()
        right_ad = models.RightAd.objects.all().filter(status=True).first()
        context = {
            'topAd': top_ad,
            'bottomAd': bottom_ad,
            'leftAd': left_ad,
            'rightAd': right_ad,
            'upload_cv_form': upload_cv_form
        }
        return render(request, 'upload_cv/upload_cv.html', context)

    def post(self, request):
        upload_cv_form = forms.UploadCVForm(request.POST)
        name = upload_cv_form['name']
        email = upload_cv_form['email']
        phone = upload_cv_form['phone']
        cv_format = upload_cv_form['cv_format']
        cv_upload = upload_cv_form['cv_upload']
        agree_to_terms = upload_cv_form['agree_to_terms']
        print(name)
        print(email)
        print(phone)
        print(cv_format)
        print(cv_upload)
        print(agree_to_terms)

        # check if form is valid
        # if upload_cv_form.is_valid():
        #     print('valid')
        #
        #     # get form data
        #     name = upload_cv_form.cleaned_data['name']
        #     email = upload_cv_form.cleaned_data['email']
        #     phone = upload_cv_form.cleaned_data['phone']
        #     cv_format = upload_cv_form.cleaned_data['cv_format']
        #     cv_upload = upload_cv_form.cleaned_data['cv_upload'].file
        #     agree_to_terms = upload_cv_form.cleaned_data['agree_to_terms']
        #
        #     # check if email exists
        #     if models.UploadCV.objects.filter(email=email).exists():
        #         msg.error(request, 'Email already exists!')
        #         return redirect('upload_cv')
        #     else:
        #         # insert data to database
        #         data = models.UploadCV.objects.create(
        #             name=name, email=email, phone=phone, cv_format=cv_format, cv_upload=cv_upload,
        #             agree_to_terms=agree_to_terms
        #         )
        #         data.save()
        #         msg.success(request, 'Uploaded Successfully')
        #         return redirect('cv_appreciation')
        #
        # else:
        #     print('invalid')
        #     msg.error(request, 'Invalid data')
        return redirect('upload_cv')


def appreciation(request):
    top_ad = models.TopAd.objects.filter(status=True).all().first()
    bottom_ad = models.BottomAd.objects.all().filter(status=True)
    left_ad = models.LeftAd.objects.all().filter(status=True).first()
    right_ad = models.RightAd.objects.all().filter(status=True).first()
    context = {
        'topAd': top_ad,
        'bottomAd': bottom_ad,
        'leftAd': left_ad,
        'rightAd': right_ad
    }
    return render(request, 'upload_cv/appreciation.html', context)
