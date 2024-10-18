from django.db import models

# Create your models here.


class WeatherEntry(models.Model):
    location = models.CharField(max_length=100)
    date = models.DateField()
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    atmospheric_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    air_humidity = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return f"{self.location}: {self.date}: {self.temperature}°C, {self.atmospheric_pressure}, {self.air_humidity}, {self.description}"



class WeatherShort(WeatherEntry):
    class Meta: 
        proxy = True
        ordering = ['location', 'date', 'temperature']


