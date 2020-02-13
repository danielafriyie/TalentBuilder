from django.shortcuts import render, redirect
from django.contrib import messages as msg
from . import models
from advertisement import models as ad_models
from django.views.generic import View
from .forms import PortfolioBannerAdQuery
from django.db import connection
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def portfolio(request):
    top_ad = ad_models.TopAd.objects.filter(status=True).all().first()
    bottom_ad = ad_models.BottomAd.objects.all().filter(status=True)[:6]
    left_ad = ad_models.LeftAd.objects.all().filter(status=True).first()
    right_ad = ad_models.RightAd.objects.all().filter(status=True).first()
    context = {
        'topAd': top_ad,
        'bottomAd': bottom_ad,
        'leftAd': left_ad,
        'rightAd': right_ad
    }

    # check for post request
    if request.method == 'POST':
        # get form data
        name = request.POST['name']
        slug_name = name.lower().replace(' ', '-')
        email = request.POST['email']
        phone = request.POST['phone']
        p_headline = request.POST['p_headline']
        about = request.POST['about']
        cv_upload = request.FILES['cv_upload']
        picture = request.FILES['picture']
        facebook = request.POST['facebook']
        twitter = request.POST['twitter']
        instagram = request.POST['instagram']
        linkedin = request.POST['linkedin']
        theme = request.POST['theme']
        agree_to_terms = request.POST['agree_to_terms']
        # banner_ad = models.PortfolioAd.objects.all().get(id=1)

        # check for existing email
        if models.Portfolio.objects.filter(email=email).exists():
            msg.error(request, 'Email already exists')
            return redirect('portfolio')
        else:
            # insert data into database
            data = models.Portfolio.objects.create(
                name=name, slug_name=slug_name, email=email, phone=phone, p_headline=p_headline, about=about,
                picture=picture, cv_upload=cv_upload, facebook=facebook, twitter=twitter,
                instagram=instagram, linkedin=linkedin, theme=theme, agree_to_terms=agree_to_terms,
            )
            data.save()
            msg.success(request, 'Form submitted successfully')
            return redirect('portfolio_appreciation')

    return render(request, 'portfolio/portfolio.html', context)


def appreciation(request):
    top_ad = ad_models.TopAd.objects.filter(status=True).all().first()
    bottom_ad = ad_models.BottomAd.objects.all().filter(status=True)[:6]
    left_ad = ad_models.LeftAd.objects.all().filter(status=True).first()
    right_ad = ad_models.RightAd.objects.all().filter(status=True).first()
    context = {
        'topAd': top_ad,
        'bottomAd': bottom_ad,
        'leftAd': left_ad,
        'rightAd': right_ad
    }
    return render(request, 'portfolio/appreciation.html', context)


def portfolio_theme(request, portfolio_id, slug_name):
    p_id = models.Portfolio.objects.get(id=portfolio_id, slug_name=slug_name)
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


def search_portfolio(request):
    # Advertisement
    top_ad = ad_models.TopAd.objects.filter(status=True).all().first()
    bottom_ad = ad_models.BottomAd.objects.all().filter(status=True)[:6]
    left_ad = ad_models.LeftAd.objects.all().filter(status=True).first()
    right_ad = ad_models.RightAd.objects.all().filter(status=True).first()

    query_set_list = models.Portfolio.objects.order_by('id')
    sent = ''
    portfolio_link = 'https://wwww.talentbuilder.top/portfolio/'

    if 'sent' in request.GET:
        sent = request.GET['sent']

    if 'email' in request.GET:
        email = request.GET['email']
        if email:
            if query_set_list.filter(email__iexact=email).exists():
                query_set_list = query_set_list.filter(email__iexact=email)
            else:
                msg.error(request, 'Email does not exist!')
                return redirect('search_portfolio')

    context = {
        'query_set_list': query_set_list,
        'sent': sent,
        'portfolio_link': portfolio_link,
        'topAd': top_ad,
        'bottomAd': bottom_ad,
        'leftAd': left_ad,
        'rightAd': right_ad
    }
    return render(request, 'portfolio/search_portfolio.html', context)


class ManagePortfolioBannerAds(View):

    @method_decorator(login_required)  # check if user is logged in and is_superuser
    def get(self, request):
        if request.user.is_superuser:
            msg.success(request, f'Welcome {request.user.username}')
            forms = PortfolioBannerAdQuery()
            return render(request, 'portfolio/manage_portfolio_banner_ads.html', {'forms': forms})
        # else:
        #     return redirect('home')

    @method_decorator(login_required)  # check if user is logged in and is_superuser
    def post(self, request):
        if request.user.is_superuser:
            forms = PortfolioBannerAdQuery(request.POST)

            if forms.is_valid():
                banner_ad_id = forms.cleaned_data['banner_ad_id']
                id_from = forms.cleaned_data['id_from']
                id_to = forms.cleaned_data['id_to']

                if ad_models.PortfolioAd.objects.all().filter(id=banner_ad_id).exists():
                    def my_custom_sql():
                        try:
                            with connection.cursor() as cursor:
                                cursor.execute(
                                    'UPDATE portfolio_portfolio SET banner_ad_id = %s WHERE id >= %s AND id <= %s',
                                    [banner_ad_id, id_from, id_to]
                                )
                        except IntegrityError:
                            msg.error(request, '<< IntegrityError, Banner Ad ID does not exist >>')
                        except:
                            msg.error(request, '<< Unexpected error, please try again! >>')
                        else:
                            msg.success(request, 'Success, updated table successfully')

                    my_custom_sql()

                    return redirect('portfolio_banner_ads')
                else:
                    msg.error(request, 'Banner Ad ID does not exist!')
                    return redirect('portfolio_banner_ads')
            else:
                msg.warning(request, 'Invalid Data')
                return redirect('portfolio_banner_ads')
        # else:
        #     return redirect('home')
