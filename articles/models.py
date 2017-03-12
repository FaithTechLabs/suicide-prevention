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

class HomeArticle(Page):
    template = 'articles/home.html'


class ArticleTag(TaggedItemBase):
        content_object = ParentalKey('ContentArticle', related_name='tagged_items')


class ContentArticle(Page):
    template = 'articles/article.html'
    date = models.DateField()

    body = StreamField([
        ('paragraph', blocks.RichTextBlock(icon='edit', template='wagtail_blocks/paragraph.html')),
        ('image', ImageChooserBlock(icon='image', template='wagtail_blocks/image.html')),
        ('full_width_image', ImageChooserBlock(icon='image', template='wagtail_blocks/full_width_image.html')),
    ])
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

class ArticleRelatedLink(Orderable):
    page = ParentalKey(ContentArticle, related_name='related_links')
    name = models.CharField(max_length=255)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
