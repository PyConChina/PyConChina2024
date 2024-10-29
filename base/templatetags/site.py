from __future__ import annotations

from datetime import time
from typing import TYPE_CHECKING

from django import template
from wagtail.models import Site

if TYPE_CHECKING:
    from schedule.models import Schedule

register = template.Library()


@register.simple_tag(takes_context=True)
def get_site_root(context):
    return Site.find_for_request(context["request"]).root_page


def get_time_delta_minutes(a: time, b: time) -> int:
    return (b.hour * 60 + b.minute) - (a.hour * 60 + a.minute)


@register.simple_tag
def get_span(schedule: Schedule, start_time: time) -> tuple[int, int]:
    return (
        get_time_delta_minutes(start_time, schedule.start_time),
        get_time_delta_minutes(start_time, schedule.end_time),
    )


@register.filter
def divide(value: int, by: int) -> int:
    return value // int(by)
