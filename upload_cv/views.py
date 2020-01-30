from django.shortcuts import render, redirect
from django.contrib import messages as msg
from django.views.generic import View
from . import models


# Function base view
def upload_cv(request):
    # Advertisements
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
    # check if it's a post request
    if request.method == 'POST':

        # get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cv_format = request.POST['cv_format']
        cv_upload = request.FILES['cv_upload']

        # check if email exists
        if models.UploadCV.objects.filter(email=email).exists():
            msg.error(request, 'Email already exists!')
            return redirect('upload_cv')
        else:
            # upload file
            data = models.UploadCV.objects.create(
                name=name, email=email, phone=phone, cv_format=cv_format, cv_upload=cv_upload
            )
            data.save()
            msg.success(request, 'Uploaded Successfully')
            return redirect('cv_appreciation')

    return render(request, 'upload_cv/upload_cv.html', context)


# Class Base View
class UploadCVView(View):

    def get(self, request):
        top_ad = models.TopAd.objects.filter(status=True).all().first()
        context = {
            'topAd': top_ad
        }
        return render(request, 'upload_cv/upload_cv.html', context)

    def post(self, request):

        # get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cv_format = request.POST['cv_format']
        cv_upload = request.FILES['cv_upload']
        agree_to_terms = request.POST['agree_to_terms']

        # check if email exists
        if models.UploadCV.objects.filter(email=email).exists():
            msg.error(request, 'Email already exists!')
            return redirect('upload_cv')
        else:
            # upload file
            data = models.UploadCV.objects.create(
                name=name, email=email, phone=phone, cv_format=cv_format, cv_upload=cv_upload,
                agree_to_terms=agree_to_terms
            )
            data.save()
            msg.success(request, 'Uploaded Successfully')
            return redirect('CVappreciation')


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
