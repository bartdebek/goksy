from django.urls import path, include

from results.views import (
    ListResults,
    PostResult,
    ListTracks,
    PostTrack
)

urlpatterns = [
    path('', ListResults.as_view(), name='my-results'),
    path('upload/', PostResult.as_view(), name='post-results'),
    path('tracks/', ListTracks.as_view(), name='tracks'),
    path('tracks/upload/', PostTrack.as_view(), name='post-tracks'),
]
