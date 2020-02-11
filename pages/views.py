from django.shortcuts import render, redirect
from . import models
from advertisement.models import BannerAdRate


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
    rate_file = BannerAdRate.objects.all().order_by('-id').first().rate.url
    return redirect(rate_file)
