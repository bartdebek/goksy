from django.contrib import admin

# Register your models here.
from .models import Result

class ResultAdmin(admin.ModelAdmin):
    fields = ["name", "fastest_lap", "date", "track_layout", "added_by"]
    list_display = ["name", "fastest_lap", "track_layout", "date", "date_added"]

admin.site.register(Result, ResultAdmin)