from django.contrib import admin
from django.urls import path
from .views import LocationListView, LocationUpdateView,FilialListView

urlpatterns = [
    path('location/', LocationListView.as_view()),
    path('location/<pk>', LocationUpdateView.as_view()),
    path('filial/', FilialListView.as_view()),
    #path('filial/<pk>', FilialUpdateView.as_view()),
]
