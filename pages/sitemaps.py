from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from datetime import datetime as dt
from portfolio.models import Portfolio


class HomePage(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['home']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class AboutPage(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['about']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class ContactPage(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['contact']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class TermsPage(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['terms']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class PrivacyPage(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['privacy']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class ClientPortfolio(Sitemap):
    changefreq = "monthly"

    def items(self):
        return Portfolio.objects.all()

    def lastmod(self, obj):
        return obj.date
