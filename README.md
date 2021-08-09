# WeatherApp

## Table of contents:
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)



## General info:
This project is a simple web-based application for finding the present weather condition of various places.

## Technologies
* Python version: 3.9.5
* Django --version: 3.3.4
* requests version: 2.26.0
* OpenWeatherAPI 
* PycharmIDE

## Setup
To setup the project install the following:

**pip install django**

**pip install requests**
#### (You can also create a virtual environment and install all the related packages into that environment so that you can create an isolated environment for your project.)

OpenWeatherAPI will allow you to get real-time weather for any cities that you've addedd to this app.

Go to the site https://openweathermap.org/api, create an account and then go to the API keys on their dashboard. You can use the Default key that they provide or you can create a new API key. This key will allow you to use the API to get the weather.

Then you can use that API key in URL defined in views.py as,
http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=Write_YOUR_APP_KEY_here

Here my API key is protected inside an environment variable, I've accessed it from the code as I do not want to reveal the key publicly. 

After setting up everything that is mentioned above, run the following command to start the project: **python manage.py runserver**








