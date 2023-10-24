from django.db.models import Avg

from results.models import Result, Track

from results.serializers import TrackSerializer

def append_avg_times(user):
    serialized_data_with_avg_lap_time = []
    tracks = Track.objects.all()

    for track in tracks:
            your_results = Result.objects.filter(added_by=user, track=track)
            your_avg_lap_time = your_results.aggregate(your_avg_lap_time=Avg('fastest_lap'))
            serialized_track = TrackSerializer(track).data
            serialized_track['your_average_lap_time'] = round(your_avg_lap_time['your_avg_lap_time'], 2)

            global_results = Result.objects.filter(track=track)
            global_avg_lap_time = global_results.aggregate(global_avg_lap_time=Avg('fastest_lap'))
            serialized_track['global_average_lap_time'] = round(global_avg_lap_time['global_avg_lap_time'], 2)

            serialized_data_with_avg_lap_time.append(serialized_track)

    return serialized_data_with_avg_lap_time