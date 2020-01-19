from django.shortcuts import render, redirect
from django.contrib import messages as msg
from django.views.generic import View
from .models import UploadCV


# Function base view
def upload_cv(request):
    # check if it's a post request
    if request.method == 'POST':

        # get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cv_format = request.POST['cv_format']
        cv_upload = request.FILES['cv_upload']

        # check if email exists
        if UploadCV.objects.filter(email=email).exists():
            msg.error(request, 'Email already exists!')
            return redirect('upload_cv')
        else:
            # upload file
            data = UploadCV.objects.create(
                name=name, email=email, phone=phone, cv_format=cv_format, cv_upload=cv_upload
            )
            data.save()
            msg.success(request, 'Uploaded Successfully')
            return redirect('appreciation')

    return render(request, 'upload_cv/upload_cv.html')


# Class Base View
class UploadCVView(View):

    def get(self, request):
        return render(request, 'upload_cv/upload_cv.html')

    def post(self, request):

        # get form data
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        cv_format = request.POST['cv_format']
        cv_upload = request.FILES['cv_upload']
        agree_to_terms = request.POST['agree_to_terms']

        # check if email exists
        if UploadCV.objects.filter(email=email).exists():
            msg.error(request, 'Email already exists!')
            return redirect('upload_cv')
        else:
            # upload file
            data = UploadCV.objects.create(
                name=name, email=email, phone=phone, cv_format=cv_format, cv_upload=cv_upload,
                agree_to_terms=agree_to_terms
            )
            data.save()
            msg.success(request, 'Uploaded Successfully')
            return redirect('CVappreciation')


def appreciation(request):
    return render(request, 'upload_cv/appreciation.html')
