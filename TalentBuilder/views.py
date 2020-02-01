from django.shortcuts import render


def deactivate_adblock(request):
    return render(request, 'deactivate_adblock.html')
