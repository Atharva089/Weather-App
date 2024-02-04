from django.shortcuts import render
import json
import urllib

# Create your views here.

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=eef72b6b3904ddf3d5c27cc58327ab80').read()

        list_of_data=json.loads(source)  #stores all the data we are requesting from the api about the climate of the city

#the following will fetch the data from json file
        data = {
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ', ' + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + ' °C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']), 
            "main": str(list_of_data['weather'][0]['main']), 
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
        }
        print(data)

    else:
        data = {}

    return render(request, "main/index.html", data)





