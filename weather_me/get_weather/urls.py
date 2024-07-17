from django.urls import path
from .views import index_view

namespace = 'weather'

urlpatterns = [
    path('weather/', index_view, name='get_weather'),
]
