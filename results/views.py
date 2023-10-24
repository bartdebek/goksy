from django.shortcuts import render

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Result
from .serializers import ResultSerializer

class ResultsView(generics.ListAPIView):
    "Display your lap results from latest to earliest"
    serializer_class = ResultSerializer
    model = Result
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        author = self.request.user
        results = Result.objects.filter(added_by=author)
        return results
    
    def perform_create(self, serializer):
        author = self.request.user
        serializer.save(added_by=author)
