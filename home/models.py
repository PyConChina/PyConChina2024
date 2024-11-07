from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField, StreamField
from wagtail import blocks
from wagtail.models import Orderable, Page, ParentalKey


class ContentBlock(blocks.StructBlock):
    title = blocks.CharBlock(required=True, form_classname="title")
    paragraph = blocks.RichTextBlock()


class HomePage(Page):
    venue = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    body = StreamField([('paragraph', ContentBlock())])

    content_panels = Page.content_panels + [
        FieldPanel("venue"),
        FieldPanel("date"),
        FieldPanel("body"),
        InlinePanel("links", heading="Related Links", label="Related Links"),
    ]


class RelatedLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=255)
    url = models.URLField()
