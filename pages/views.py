from django.shortcuts import render, redirect
from . import models


def home(request):
    return render(request, 'pages/index.html')


def about(request):
    return render(request, 'pages/about.html')


def contact(request):
    return render(request, 'pages/contact.html')


def terms(request):
    return render(request, 'pages/terms_and_conditions.html')


def privacy(request):
    return render(request, 'pages/privacy_policy.html')


def banner_ads(request):
    rate_file = models.BannerAds.objects.all().order_by('-id').first().rate.url

    return redirect(rate_file)
