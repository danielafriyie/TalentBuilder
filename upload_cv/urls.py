from django.urls import path
from . import views


urlpatterns = [
    path('', views.upload_cv, name='upload_cv'),
    path('appreciation/', views.appreciation, name='cv_appreciation')
]
