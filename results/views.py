from django.db.models import Avg

from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from results.models import Result, Track
from results.serializers import ResultSerializer, TrackSerializer

from results.utils import append_avg_times

class ListResults(generics.ListAPIView):
    """Display your lap results from latest to earliest"""
    serializer_class = ResultSerializer
    model = Result
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Result.objects.all()

    def get_queryset(self):
        author = self.request.user
        queryset = Result.objects.filter(added_by=author)
        return queryset

    def get(self, request, format=None):
        results = self.get_queryset()
        serializer = ResultSerializer(results, many=True)
        return Response(serializer.data)


class PostResult(generics.CreateAPIView):
    """Post a Result model instance"""
    serializer_class = ResultSerializer
    model = Result
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(added_by=author)


class ListTracks(generics.ListAPIView):
    """Display your lap results from latest to earliest"""
    serializer_class = TrackSerializer
    model = Track
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Track.objects.all()
        return queryset

    def get(self, request, format=None):
        user = self.request.user
        serialized_data = append_avg_times(user=user)

        return Response(serialized_data)


class PostTrack(generics.CreateAPIView):
    """Post a Track model instance"""
    serializer_class = TrackSerializer
    model = Track
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(added_by=author)

