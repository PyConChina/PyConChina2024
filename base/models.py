from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.settings.models import (
    BaseGenericSetting,
    register_setting,
)
from wagtail.models import Orderable, ParentalKey


@register_setting
class NavigationSettings(BaseGenericSetting, ClusterableModel):
    panels = [
        InlinePanel("social_links", label="Social Links"),
    ]


class SocialLink(Orderable):
    page = ParentalKey("base.NavigationSettings", related_name="social_links")
    name = models.CharField(max_length=32)
    url = models.URLField()
    icon = models.CharField(max_length=32, blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("url"),
        FieldPanel("icon"),
    ]
