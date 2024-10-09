from wagtail.blocks import (
    CharBlock,
    ListBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock


class SupporterBlock(StructBlock):
    name = CharBlock(required=True)
    description = CharBlock(required=False)
    logo = ImageChooserBlock(required=False)
    url = URLBlock(required=False)


class SupporterListBlock(StructBlock):
    heading = CharBlock(required=True)
    supporters = ListBlock(SupporterBlock())

    class Meta:
        template = "supporter/blocks/supporter-list.html"


class SupporterStreamBlock(StreamBlock):
    paragraph = RichTextBlock(required=False)
    supporters = ListBlock(SupporterListBlock())
