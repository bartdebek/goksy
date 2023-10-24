from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from .models import Result

import datetime


class ResultSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username', default=serializers.CurrentUserDefault())

    class Meta:
        model = Result
        fields = [
            "name",
            "fastest_lap",
            "track_layout",
            "date",
            "date_string",
            "added_by"
        ]
        validators = UniqueValidator(queryset=Result.objects.all())
        