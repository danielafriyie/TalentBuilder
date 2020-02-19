from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from datetime import datetime as dt


class UploadCVSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['upload_cv']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class UploadCVSearchSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['search-cv']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')


class UploadCVAppreciationSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return ['cv_appreciation']

    def location(self, obj):
        return reverse(obj)

    def lastmod(self, obj):
        return dt.strptime('2020-02-19', '%Y-%m-%d')
