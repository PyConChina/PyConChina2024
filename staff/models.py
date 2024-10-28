from django import forms
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page
from wagtail.snippets.models import register_snippet

# Create your models here.


class StaffPage(Page):
    parent_page_types = ["home.HomePage"]
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("staff_categories", label="Staff Categories"),
    ]


class StaffCategory(Orderable, ClusterableModel):
    page = ParentalKey(
        StaffPage, on_delete=models.CASCADE, related_name="staff_categories"
    )
    name = models.CharField(max_length=64)
    staff = ParentalManyToManyField("staff.Staff")

    panels = [
        FieldPanel("name"),
        FieldPanel("staff", widget=forms.CheckboxSelectMultiple),
    ]


@register_snippet
class Staff(models.Model):
    name = models.CharField(max_length=32)
    bio = models.CharField(max_length=255, blank=True)
    avatar = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("bio"),
        FieldPanel("avatar"),
    ]

    class Meta:
        verbose_name = "Staff"
        verbose_name_plural = "Staff"

    def __str__(self) -> str:
        return self.name
