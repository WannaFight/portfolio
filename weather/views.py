import os

from django.shortcuts import render, redirect
import requests


WEATHER_URL = "https://api.weatherapi.com/v1"

PARAMS = {
    "key": os.getenv('WEATHER_KEY', ''),
    "q": "moscow",
}


# Create your views here.
def index(request):
    if request.method == 'POST':
        return redirect('weather:current')
    elif request.method == 'GET':
        if request.session.get('location', ''):
            return redirect('weather:current')
        else:
            return render(request, 'weather/index.html')


def current(request):
    if request.method == 'POST':
        location = request.POST['location']
        request.session['location'] = location
    else:
        location = request.session.get('location', '')

    PARAMS['q'] = location

    resp = requests.get(f"{WEATHER_URL}/current.json", params=PARAMS)

    # 404 or something - instant render
    if not resp.ok:
        context = {
            'code': 400,
            'error_message': resp.json()['error']['message'],
        }

        return render(request, 'weather/current.html', context=context)

    resp = resp.json()

    context = {
        'code': 200,
        'city': {
            'name': resp['location']['name'],
            'country': resp['location']['country'],
        },
        'weather': {
            'time': resp['current']['last_updated'].split(' ')[-1],
            'temp': int(round(resp['current']['temp_c'], 0)),
            'temp_feels_like': int(round(resp['current']['feelslike_c'], 0)),
            'description': resp['current']['condition']['text'],
            'icon': resp['current']['condition']['icon'],
            'wind_speed': round(resp['current']['wind_kph']/3.6, 1),
            'wind_dir': resp['current']['wind_dir'],
            'humidity': resp['current']['humidity'],
            'pressure': round(resp['current']['pressure_mb']/1.333),
        }
    }

    return render(request, 'weather/current.html', context=context)


def reset_location(request):
    if request.session.get('location', ''):
        del request.session['location']
    return redirect('weather:index')
