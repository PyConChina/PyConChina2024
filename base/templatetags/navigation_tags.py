from django import template
from wagtail.models import Site

register = template.Library()


# ... keep the definition of get_footer_text and add the get_site_root template tag:
@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page
