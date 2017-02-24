from wagtail.wagtailcore.models import Page
from articles.models import ContentArticle
from django import template

register = template.Library()

@register.simple_tag
def get_articles():
   pages = ContentArticle.objects.all()
   return pages
