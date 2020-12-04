from wagtail.core.fields import StreamField
from wagtail.core.models import Page
from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock
from pages.snippet.seo import Seo
from wagtail.snippets.edit_handlers import SnippetChooserPanel


class ItemsBlock(blocks.StreamBlock):
    item = blocks.StructBlock([
        ('title', blocks.CharBlock()),
        ('image', ImageChooserBlock(required=False)),
        ('body', blocks.RichTextBlock(required=False)),
    ])


class PortfolioPage(Page):
    items = StreamField(ItemsBlock(), blank=True)

    seo = models.ForeignKey(
        Seo,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('items'),
        SnippetChooserPanel('seo'),
    ]

