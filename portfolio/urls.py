from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('appreciation/', views.appreciation, name='portfolio_appreciation'),
    path('search-portfolio/', views.search_portfolio, name='search_portfolio'),
    path('manage-portfolio-banner-ads', views.ManagePortfolioBannerAds.as_view(), name='portfolio_banner_ads'),
    path('<int:client_id>.<slug:slug_name>/', views.portfolio_theme, name='theme')
]
