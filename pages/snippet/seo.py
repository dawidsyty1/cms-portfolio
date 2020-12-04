from django.db import models
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.core.fields import StreamField


@register_snippet
class Seo(models.Model):
    name = models.CharField(max_length=255, default='')

    seo = StreamField([
        ('tag', blocks.RawHTMLBlock()),
    ], blank=True)

    panels = [
        FieldPanel('name'),
        StreamFieldPanel('seo'),
    ]

    def __str__(self):
        return self.name
