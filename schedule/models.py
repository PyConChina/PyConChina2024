from __future__ import annotations

from datetime import date, datetime, timezone

from django.db import models
from django.db.models import QuerySet
from django.http import HttpResponse
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.contrib.routable_page.models import RoutablePageMixin, path
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page, ParentalKey
from wagtail.snippets.models import register_snippet


# Create your models here.
class ScheduleListPage(RoutablePageMixin, Page):
    parent_page_types = ["home.HomePage"]
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("schedules", heading="Schedules", label="Schedules"),
    ]

    def grouped_schedules(self) -> dict[date, dict[Room | str, list[Schedule]]]:
        result: dict[date, dict[Room | str, list[Schedule]]] = {}
        schedules: QuerySet[Schedule] = self.schedules.order_by("date", "start_time")
        for schedule in schedules:
            result.setdefault(schedule.date, {}).setdefault(
                schedule.room or "none_type", []
            ).append(schedule)
        return result

    @path("ical/")
    def ical(self, request):
        from icalendar import Calendar, Event

        cal = Calendar()
        schedules: QuerySet[Schedule] = self.schedules.order_by("date", "start_time")
        for schedule in schedules:
            event = Event()
            if schedule.room:
                location = f"{schedule.room.name} ({schedule.room.address})"
            else:
                location = "主会场"
            event.add("summary", str(schedule))
            event.add("dtstart", datetime.combine(schedule.date, schedule.start_time))
            event.add("dtend", datetime.combine(schedule.date, schedule.start_time))
            event.add("dtstamp", datetime.now(timezone.utc))
            event.add("location", location)
            if schedule.talk:
                event.add(
                    "description",
                    f"演讲人：{schedule.talk.authors.first().name}\n\n{schedule.talk.body}",
                )
                event.add("url", request.build_absolute_uri(schedule.talk.url))
            cal.add_component(event)

        response = HttpResponse(cal.to_ical(), content_type="text/calendar")
        response["Content-Disposition"] = 'attachment; filename="pycon-china-2024.ics"'
        return response


class Schedule(Orderable):
    page = ParentalKey(
        "schedule.ScheduleListPage",
        on_delete=models.CASCADE,
        related_name="schedules",
    )
    talk = models.OneToOneField(
        "talk.TalkPage",
        on_delete=models.SET_NULL,
        related_name="schedule",
        null=True,
        blank=True,
    )
    name = models.CharField(
        max_length=255, help_text="Name of the schedule", blank=True
    )
    start_time = models.TimeField(help_text="Start time")
    end_time = models.TimeField(help_text="End time")
    date = models.DateField(help_text="Date of the schedule")
    room = models.ForeignKey(
        "schedule.Room",
        on_delete=models.SET_NULL,
        related_name="schedules",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.talk.title if self.talk else self.name

    panels = [
        FieldPanel("talk"),
        FieldPanel("name"),
        FieldPanel("start_time"),
        FieldPanel("end_time"),
        FieldPanel("date"),
        FieldPanel("room"),
    ]


@register_snippet
class Room(models.Model):
    name = models.CharField(max_length=32, help_text="Name of the room")
    address = models.CharField(
        max_length=255, help_text="Address of the room", blank=True
    )
    host = models.CharField(max_length=32, help_text="Host of the room", blank=True)
    panels = [FieldPanel("name"), FieldPanel("address"), FieldPanel("host")]

    def __str__(self) -> str:
        return self.name
