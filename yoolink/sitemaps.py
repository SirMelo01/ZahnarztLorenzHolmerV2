from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.utils import timezone


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "kontakt",
            "impressum",
            "datenschutz",
            "cookies",
        ]

    def lastmod(self, item):
        return timezone.now()

    def location(self, item):
        return reverse(item)
