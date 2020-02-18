from django.shortcuts import render, redirect
from . import models
from advertisement.models import BannerAdRate
from portfolio.models import Portfolio


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


def client_portfolio_theme(request, slug_name, client_id):
    p_id = Portfolio.objects.get(slug_name=slug_name, id=client_id)
    context = {
        'portfolio': p_id,
    }

    # theme check
    if p_id.theme == 'black theme':
        return render(request, 'portfolio/black_theme.html', context)
    elif p_id.theme == 'blue theme':
        return render(request, 'portfolio/blue_theme.html', context)
    elif p_id.theme == 'green theme':
        return render(request, 'portfolio/green_theme.html', context)
    elif p_id.theme == 'nano theme':
        return render(request, 'portfolio/nano_theme.html', context)
