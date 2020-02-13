from django import forms


class PortfolioBannerAdQuery(forms.Form):
    banner_ad_id = forms.IntegerField()
    id_from = forms.IntegerField()
    id_to = forms.IntegerField()
