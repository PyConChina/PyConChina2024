from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page, ParentalKey


class TalkType(models.TextChoices):
    KEYNOTE = "keynote", "Keynote"
    LIGHTNING = "lightning", "Lightning"


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

    content_panels = Page.content_panels + [
        InlinePanel("authors", heading="Authors", label="Authors"),
        FieldPanel("abstract"),
        FieldPanel("body"),
        FieldPanel("type"),
    ]


class Author(Orderable):
    page = ParentalKey(TalkPage, on_delete=models.CASCADE, related_name="authors")
    name = models.CharField(max_length=255, help_text="Name of the author")
    avatar = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )
    bio = models.CharField(max_length=255, blank=True, help_text="Bio of the author")
    introduction = RichTextField(blank=True, help_text="Introduction of the author")
