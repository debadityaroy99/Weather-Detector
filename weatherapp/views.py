from django.shortcuts import render,redirect
import json
import urllib.request
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        try:
            city = request.POST['city']
            res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&appid=cb771e45ac79a4e8e2205c0ce66ff633').read()
            json_data = json.loads(res)
            data = {
                "country_code": str(json_data['sys']['country']),
                "coordinate": str(json_data['coord']['lon']) + ' ' +
                str(json_data['coord']['lat']),
                "temp": str(json_data['main']['temp'])+'k',
                "pressure": str(json_data['main']['pressure']),
                "humidity": str(json_data['main']['humidity']),
            }

            return render(request, 'index.html', {'city': city, 'data': data})
        except urllib.error.HTTPError as http_err:
            if http_err.code == 404:
                messages.info(request,"City does not exist")
                return redirect('index')
    
    else:
        city = ''
        data = {}       
        return render(request, 'index.html', {'city': city, 'data': data})