from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from upload_cv.sitemaps import UploadCVSitemap, UploadCVSearchSitemap, UploadCVAppreciationSitemap
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import HomePage, AboutPage, ContactPage, TermsPage, PrivacyPage, ClientPortfolio
from portfolio.sitemaps import PortfolioAppreciation, PortfolioPage, PortfolioSearch


sitemaps = {
    'home': HomePage,
    'about': AboutPage,
    'contact': ContactPage,
    'upload-cv': UploadCVSitemap,
    'portfolio': PortfolioPage,
    'terms': TermsPage,
    'privacy': PrivacyPage,
    'upload-cv-search': UploadCVSearchSitemap,
    'upload-cv-appreciation': UploadCVAppreciationSitemap,
    'portfolio-appreciation': PortfolioAppreciation,
    'portfolio-search': PortfolioSearch,
    'client-portfolio': ClientPortfolio
}

urlpatterns = [
    path('', include('pages.urls')),
    path('upload-cv/', include('upload_cv.urls')),
    path('portfolio/', include('portfolio.urls')),
    path('blog/', include('blog.urls')),
    path('talentbuilderadministration1798/', admin.site.urls),
    path('deactivate-adblock/', views.deactivate_adblock, name='deactivate-adblock'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps})
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
