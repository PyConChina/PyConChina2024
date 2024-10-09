from django import forms
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page
from wagtail.snippets.models import register_snippet

# Create your models here.


class SupporterPage(Page):
    parent_page_types = ["home.HomePage"]
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("supporters", label="Supporters"),
    ]


class SupporterTier(Orderable):
    page = ParentalKey(
        SupporterPage, on_delete=models.CASCADE, related_name="supporters"
    )
    name = models.CharField(max_length=64)
    supporters = ParentalManyToManyField("supporter.Supporter")

    panels = [
        FieldPanel("name"),
        FieldPanel("supporters", widget=forms.CheckboxSelectMultiple),
    ]


@register_snippet
class Supporter(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True)
    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    url = models.URLField(blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("description"),
        FieldPanel("logo"),
        FieldPanel("url"),
    ]

    def __str__(self) -> str:
        return self.name
