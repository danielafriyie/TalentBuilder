from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', include('pages.urls')),
    path('upload-cv/', include('upload_cv.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('talentbuilderadministration1798/', admin.site.urls),
    path('deactivate-adblock/', views.deactivate_adblock, name='deactivate-adblock')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
