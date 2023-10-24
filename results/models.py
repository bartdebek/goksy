from django.db import models
from django.contrib.auth.models import User


class Track(models.Model):
    LAYOUT_CHOICES = (
        ("short", "short"),
        ("long", "long"),
    )
    name = models.CharField(max_length=255)
    layout = models.CharField(choices=LAYOUT_CHOICES, max_length=255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.layout}"


class Result(models.Model):
    name = models.CharField(max_length=255)
    fastest_lap = models.DecimalField(max_digits=7, decimal_places=3)
    track = models.ForeignKey(Track, on_delete=models.CASCADE)
    date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now=True)

    def date_string(self):
        return self.date.strftime("%d.%m.%Y")

    class Meta:
        ordering = ('-date', "fastest_lap", "track")

    def __str__(self):
        return self.date_string()