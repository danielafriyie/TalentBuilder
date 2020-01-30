from django.shortcuts import render, redirect
from django.contrib import messages as msg
from . import models


def portfolio(request):
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
        banner_ad = models.TopAd.objects.all().get(id=1)

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
                banner_ad=banner_ad
            )
            data.save()
            msg.success(request, 'Form submitted successfully')
            return redirect('portfolio_appreciation')

    return render(request, 'portfolio/portfolio.html', context)


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
