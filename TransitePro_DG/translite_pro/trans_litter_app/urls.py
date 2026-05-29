from django.urls import path
from . import views

urlpatterns = [
    path('', views.site, name='site'),
    path('api/transliterate/', views.trans_litter_text, name='transliterate'),
    path('api/', views.trans_litter_api, name='transliterate_api'),
    path('history/', views.get_history, name='history'),
]

