from tkinter import EXCEPTION
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=65fdb0769cfd0a48a69583683496a4a6'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save() #It will both validate and save the new city name to the databaseat hte same time

    form = CityForm()

    cities = City.objects.all()
    weather_list = []
    try:
        for city in cities:

            r = requests.get(url.format(city)).json()

            weather = {
                'city': city.name, # city or city.name, city print the object that contains city name, and city.name directly print the city name.
                'temperature': r['main']['temp'],
                'pressure': r['main']['pressure'],
                'humidity': r['main']['humidity'],
                'wind': r['wind']['speed'],
                'description': r['weather'][0]['description'], # 0 means first item in the list 'weather'
                'icon': r['weather'][0]['icon']
            }

            weather_list.append(weather)
    except KeyError:
        pass
    except EXCEPTION as e:
        pass
    print(weather_list)

    context = {'weather_list': weather_list, 'form': form}
    return render(request, 'design/index.html', context)





