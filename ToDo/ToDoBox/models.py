import datetime
from django.db import models
from datetime import date
from django.db.models import Count


class ToDoText(models.Model):
    text = models.CharField(max_length=300)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.text


def get_stats_data():
    start_day = datetime.date.today() - datetime.timedelta(days=8)
    items = ToDoText.objects.values('date').annotate(number_of_activities=Count('date')).filter(date__gt=start_day)
    return items


