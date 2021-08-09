from tkinter import EXCEPTION
from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
import os 


apiId = os.environ['weatherapp_api_key']

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=%s' %apiId
    cities = City.objects.all()


    error_msg = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = CityForm(request.POST)
        # form.save()

        if form.is_valid():
            new_city = form.cleaned_data['name']
            existing_city_count = City.objects.filter(name=new_city).count()

            if existing_city_count == 0:
                r = requests.get(url.format(new_city)).json()
                
                if r['cod'] == 200:
                    form.save()
                else:
                    error_msg = 'City doesnot exists.'
            else:
                error_msg = 'City already exists in the database!'

        if error_msg:
            message = error_msg
            message_class = 'is-danger'
        else:
            message = 'City added successfully'
            message_class= 'is-success'


    # if request.method == 'POST':
    #     form = CityForm(request.POST)
    #     form.save() #It will both validate and save the new city name to the databaseat hte same time

    
    form = CityForm()
    
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

    context = {'weather_list': weather_list, 
                'form': form,
                 'message': message,
                 'message_class':message_class}
    return render(request, 'design/index.html', context)





