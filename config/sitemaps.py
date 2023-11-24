from django.contrib.sitemaps import Sitemap
from django.db.models.base import Model
from django.urls import reverse
from django.shortcuts import reverse

 


class StaticViewSitemap(Sitemap):
    def items(self):
        return ['index', 'show']
    
    def location(self, item):
        return reverse(item)
    




