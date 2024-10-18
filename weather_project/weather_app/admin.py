from django.contrib import admin 
from .models import WeatherEntry
from .models import WeatherShort

# Register your models here.

@admin.register(WeatherEntry)
class WeatherEntryAdmin(admin.ModelAdmin):
    list_display = ['location', 'date', 'temperature', 'atmospheric_pressure', 'air_humidity', 'description']

# @admin.register(WeatherShort)