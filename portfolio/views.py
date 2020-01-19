from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages as msg
from .models import Portfolio


def portfolio(request):
    # meta description content
    content = 'Free Portfolio Website'

    # check for post request
    if request.method == 'POST':
        # get form data
        name = request.POST['name']
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

        # check for existing email
        if Portfolio.objects.filter(email=email).exists():
            msg.error(request, 'Email already exists')
            return redirect('portfolio')
        else:
            # insert data into database
            data = Portfolio.objects.create(
                name=name, email=email, phone=phone, p_headline=p_headline, about=about,
                picture=picture, cv_upload=cv_upload, facebook=facebook, twitter=twitter,
                instagram=instagram, linkedin=linkedin, theme=theme, agree_to_terms=agree_to_terms
            )
            data.save()
            msg.success(request, 'Form submitted successfully')
            return redirect('portfolio_appreciation')

    return render(request, 'portfolio/portfolio.html', {'content': content})


def appreciation(request):
    return render(request, 'portfolio/appreciation.html')


def portfolio_theme(request, portfolio_id, portfolio_name):
    p_id = get_object_or_404(Portfolio, pk=portfolio_id)
    context = {
        'portfolio': p_id
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
