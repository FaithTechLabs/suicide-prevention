from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse, resolve

def get_sitemap():
    sitemap = {
        "main_sitemap": MainSitemap,
        "province_sitemap": ProvinceSitemap,
    }
    return sitemap

class MainSitemap(Sitemap):
    """
    For highest priority pages
    """

    priority = 1.0

    def items(self):
        return ['/', '/why/', '/chat/', '/why_we_are_here/', '/resource/']

    def location(self, item):
	return item

class ProvinceSitemap(Sitemap):
    """
    Loops through all provinces
    """

    priority = 0.5

    def items(self):
        pages = ["/alberta/", "/british_columbia/", "/manitoba/", "/new_brunswick/", "/newfoundland/", "/nova_scotia/", \
                "/ontario/", "/pei/", "/northwest_territories/", "/quebec/", "/saskatchewan/", "/yukon/", "/nunavut/"]
        return pages

    def location(self, item):
	return "/province" + item

