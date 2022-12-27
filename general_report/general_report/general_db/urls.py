from django.contrib import admin
from django.urls import path
from .views import LocationListView, LocationUpdateView

urlpatterns = [
    path('location/', LocationListView.as_view()),
    path('location/<pk>', LocationUpdateView.as_view()),
]
