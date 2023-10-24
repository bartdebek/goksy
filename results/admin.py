from django.contrib import admin

# Register your models here.
from results.models import Result, Track

class ResultAdmin(admin.ModelAdmin):
    fields = ["name", "fastest_lap", "date", "track", "added_by"]
    list_display = ["name", "fastest_lap", "track", "date", "date_added"]

class TrackAdmin(admin.ModelAdmin):
    fields = ["name", "layout", "added_by"]
    list_display = ["__str__", "added_by", "date_added"]

admin.site.register(Result, ResultAdmin)
admin.site.register(Track, TrackAdmin)