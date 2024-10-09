from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page

from supporter.blocks import SupporterStreamBlock

# Create your models here.


class SupporterPage(Page):
    parent_page_types = ["home.HomePage"]

    body = StreamField(
        SupporterStreamBlock(),
        use_json_field=True,
        help_text="Add supporters to the page.",
    )

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]
