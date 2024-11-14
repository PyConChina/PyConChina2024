from django import forms
from django.db import models
from modelcluster.fields import ParentalManyToManyField
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class TalkType(models.TextChoices):
    KEYNOTE = "keynote", "主题"
    LIGHTNING = "lightning", "闪电"
    ROUNDTABLE = "roundtable", "圆桌"


# Create your models here.
class TalkListPage(Page):
    parent_page_types = ["home.HomePage"]
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class TalkPage(Page):
    parent_page_types = ["talk.TalkListPage"]
    abstract = models.TextField(blank=True)
    body = RichTextField(blank=True)
    type = models.CharField(
        max_length=32, choices=TalkType.choices, default=TalkType.KEYNOTE
    )
    authors = ParentalManyToManyField("talk.Author")

    content_panels = Page.content_panels + [
        FieldPanel("authors", widget=forms.CheckboxSelectMultiple),
        FieldPanel("abstract"),
        FieldPanel("body"),
        FieldPanel("type"),
    ]


@register_snippet
class Author(models.Model):
    name = models.CharField(max_length=255, help_text="Name of the author")
    avatar = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    bio = models.CharField(max_length=255, blank=True, help_text="Bio of the author")
    introduction = RichTextField(blank=True, help_text="Introduction of the author")

    panels = [
        FieldPanel("name"),
        FieldPanel("avatar"),
        FieldPanel("bio"),
        FieldPanel("introduction"),
    ]

    def __str__(self):
        return self.name
