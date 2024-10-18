from django.shortcuts import render, redirect, get_object_or_404
from .models import WeatherEntry, WeatherShort
from .forms import WeatherEntryForm

def index(request):
    weather_short = WeatherShort.objects.all() 
    return render(request, 'weather_app/index.html', {'weather_short': weather_short})

def add_entry(request):
    if request.method == 'POST':
        form = WeatherEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = WeatherEntryForm()
   
    return render(request, 'weather_app/add_entry.html', {'form': form})

def entry_detail(request, entry_id):
    entry = get_object_or_404(WeatherEntry, id=entry_id)
    return render(request, 'weather_app/entry_detail.html', {'entry': entry})
   