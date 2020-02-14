from django.shortcuts import render, redirect
from . import models
from advertisement.models import BannerAdRate
from django.core.mail import send_mail
from django.http import HttpResponse
from upload_cv.models import UploadCVMailMessage


def home(request):
    testimonials = models.Testimonials.objects.order_by('-id').all()[:4]
    short_list = models.ShortListCompanies.objects.order_by('-id').all()
    context = {
        'testimonials': testimonials,
        'short_list': short_list
    }
    return render(request, 'pages/index.html', context)


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def terms(request):
    return render(request, 'pages/terms_and_conditions.html')


def privacy(request):
    return render(request, 'pages/privacy_policy.html')


def banner_ads(request):
    try:
        rate_file = BannerAdRate.objects.all().order_by('-id').first().rate.url
        return redirect(rate_file)
    except AttributeError:
        return redirect('home')
    except ValueError:
        return redirect('home')


# def my_mail(request):
#     email_msg = UploadCVMailMessage.objects.order_by('-date').all().first()
#     msg_body = f'{email_msg.before_msg} Danny {email_msg.after_msg}'
#     send_mail(
#         email_msg.subject,
#         msg_body,
#         email_msg.host_user.host_user,
#         ['danielafriyie98@gmail.com', 'afriyiedaniel1@outlook.com'],
#         fail_silently=False,
#     )
#     return HttpResponse('<h1>EMAIL SENT</h1>')
