# Generated by Django 4.2.16 on 2024-10-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('atmospheric_pressure', models.DecimalField(decimal_places=2, max_digits=5)),
                ('air_humidity', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='WeatherShort',
            fields=[
            ],
            options={
                'ordering': ['location', 'date', 'temperature'],
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('weather_app.weatherentry',),
        ),
    ]
