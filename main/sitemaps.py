# main/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import Post  # replace with your actual model if different

class StaticViewSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ['login', 'signup', 'home', 'admin', 'forgot_password', 'appoinments']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6

    def items(self):
        return Post.objects.all()

    def location(self, obj):
        return reverse('view_product', kwargs={'post_id': str(obj.pk)})
