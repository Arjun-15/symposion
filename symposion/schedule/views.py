from django.http import Http404
from django.shortcuts import render, get_object_or_404

from symposion.schedule.models import Schedule, Day
from symposion.schedule.timetable import TimeTable


def schedule_detail(request, slug=None):
    qs = Schedule.objects.all()
    if slug is None:
        schedule = next(iter(qs), None)
        if schedule is None:
            raise Http404()
    else:
        schedule = get_object_or_404(qs, slug=slug)
    ctx = {
        "schedule": schedule,
    }
    return render(request, "schedule/schedule_detail.html", ctx)


def schedule_edit(request, slug=None):
    qs = Schedule.objects.all()
    if slug is None:
        schedule = next(iter(qs), None)
        if schedule is None:
            raise Http404()
    else:
        schedule = get_object_or_404(qs, slug=slug)
    days_qs = Day.objects.filter(schedule=schedule)
    days = [TimeTable(day) for day in days_qs]
    ctx = {
        "schedule": schedule,
        "days": days,
    }
    return render(request, "schedule/schedule_edit.html", ctx)