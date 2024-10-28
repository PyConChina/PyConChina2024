from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page, ParentalKey


class HomePage(Page):
    venue = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    about = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("venue"),
        FieldPanel("date"),
        FieldPanel("about"),
        InlinePanel("links", heading="Related Links", label="Related Links"),
    ]


class RelatedLink(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name="links")
    title = models.CharField(max_length=255)
    url = models.URLField()
