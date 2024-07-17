from django.shortcuts import render
from .utils import get_weather
from .forms import CityForm


def index_view(request):
    context = {}
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            context = get_weather(city)
    else:
        form = CityForm()
    context['form'] = form
    return render(request, 'index.html', context)
