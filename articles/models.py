from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore import blocks
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index
from modelcluster.fields import ParentalKey
from modelcluster.tags import ClusterTaggableManager
from taggit.models import TaggedItemBase

"""Basic template for the article index page

   Args:
        Page (:class:`Page`): A wagtail page object

"""
class HomeArticle(Page):
    template = 'articles/home.html'


"""Tags for article categories

   Args:
        TaggedItemBase (:class:`TaggedItemBase`): A wagtail tag object

"""
class ArticleTag(TaggedItemBase):
    content_object = ParentalKey('ContentArticle', related_name='tagged_items')


""" Template for articles

    Uses the wagtail stream field so that users can add in custom blocks that
    can be used in the CMS such as paragraphs of images. Blocks are added to the
    body StreamField.

   Args:
        Page (:class:`Page`): A wagtail page object

"""
class ContentArticle(Page):
    template = 'articles/article.html'
    date = models.DateField()

    # Each block will show up when adding elements to a page in the CMS
    body = StreamField([
        ('paragraph', blocks.RichTextBlock(icon='edit', template='wagtail_blocks/paragraph.html')),
        ('image', ImageChooserBlock(icon='image', template='wagtail_blocks/image.html')),
        ('full_width_image', ImageChooserBlock(icon='image', template='wagtail_blocks/full_width_image.html')),
    ])

    # We want to be able to tag articles with certain categories
    tags = ClusterTaggableManager(through=ArticleTag, blank=True)

    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    author = models.CharField(max_length=200, null=True, blank=True)

    search_fields = Page.search_fields + [
        index.FilterField('title'),
        index.FilterField('author'),
        index.SearchField('body'),
        index.FilterField('date'),
    ]
    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('tags'),
        FieldPanel('author'),
        StreamFieldPanel('body'),
        InlinePanel('related_links', label="Related links"),
    ]

"""Allows adding related links to articles

   Args:
        Orderable (:class:`Orderable`): Wagtail object for related links

"""
class ArticleRelatedLink(Orderable):
    page = ParentalKey(ContentArticle, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
