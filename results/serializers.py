from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from results.models import Result, Track

import datetime


class ResultSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username', default=serializers.CurrentUserDefault())

    class Meta:
        model = Result
        fields = [
            "name",
            "fastest_lap",
            "track",
            "date",
            "date_string",
            "added_by"
        ]
        validators = UniqueValidator(queryset=Result.objects.all())


class TrackSerializer(serializers.ModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username', default=serializers.CurrentUserDefault())

    class Meta:
        model = Track
        fields = [
            "name",
            "layout",
            "added_by",
            "date_added"
        ]
        validators = UniqueValidator(queryset=Result.objects.all())
        