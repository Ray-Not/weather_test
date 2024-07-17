from django.shortcuts import render
from .utils import get_weather


def index_view(request):
    context = get_weather('Moscow')
    # context = {}
    return render(request, 'index.html', context)
