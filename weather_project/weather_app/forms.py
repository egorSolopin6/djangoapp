from django import forms
from .models import WeatherEntry

class WeatherEntryForm(forms.ModelForm):
    class Meta:
        model = WeatherEntry
        fields = ['location', 'date', 'temperature', 'atmospheric_pressure', 'air_humidity', 'description']

