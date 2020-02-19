from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from datetime import datetime as dt


class PortfolioPage(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['portfolio']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class PortfolioAppreciation(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['portfolio_appreciation']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class PortfolioSearch(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['search_portfolio']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')
