from django.urls import path
from . import views


urlpatterns = [
    path('', views.UploadCVView.as_view(), name='upload_cv'),
    path('appreciation/', views.appreciation, name='CVappreciation')
]
