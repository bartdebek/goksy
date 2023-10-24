from django.urls import path, include

from .views import (
    ResultsView
)

urlpatterns = [
    path('my-results/', ResultsView.as_view(), name='my-results')
]
