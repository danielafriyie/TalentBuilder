from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio, name='portfolio'),
    path('appreciation/', views.appreciation, name='portfolio_appreciation'),
    path('<int:portfolio_id>/<str:portfolio_name>/', views.portfolio_theme, name='theme'),
]
