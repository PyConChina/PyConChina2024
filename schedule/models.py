from django.db import models
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.fields import RichTextField
from wagtail.models import Orderable, Page, ParentalKey
from wagtail.snippets.models import register_snippet


# Create your models here.
class ScheduleListPage(Page):
    parent_page_types = ["home.HomePage"]
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        InlinePanel("schedules", heading="Schedules", label="Schedules"),
    ]


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
    panels = [FieldPanel("name"), FieldPanel("address")]

    def __str__(self) -> str:
        return self.name
