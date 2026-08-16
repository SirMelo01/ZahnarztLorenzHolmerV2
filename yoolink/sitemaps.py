from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from django.utils import timezone
from django.utils.translation import get_language

from yoolink.ycms.models import Blog


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    def items(self):
        return [
            "home",
            "blog:blog",
            "impressum",
            "datenschutz",
            "cookies",
        ]

    def lastmod(self, item):
        return timezone.now()

    def location(self, item):
        return reverse(item)


class BlogSitemap(Sitemap):
    """Die einzelnen Blog-Detailseiten.

    Uebersetzungen sind eigene Blog-Datensaetze mit gesetztem ``original``; der
    Filter auf ``language`` liefert deshalb pro Sprache genau die passende
    Variante und keine Duplikate.
    """

    changefreq = "weekly"

    def items(self):
        lang = get_language() or "de"
        return Blog.objects.filter(active=True, language=lang).order_by("-last_updated")

    def lastmod(self, obj):
        return obj.last_updated
