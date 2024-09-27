from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    venue = models.CharField(max_length=255, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    about = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("venue"),
        FieldPanel("date"),
        FieldPanel("about"),
    ]
