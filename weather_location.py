# importing requests and json
import requests

# getting location data
ip_request = requests.get('https://get.geojs.io/v1/ip.json')
ipAdd = ip_request.json()['ip']
url = 'https://get.geojs.io/v1/ip/geo/' + ipAdd +'.json'
geo_request = requests.get(url)
geo_data = geo_request.json()

def weather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = geo_data['city']
    API_KEY = "7286a00b1d1ba04c8247afe737c5bab2"
    # upadting the URL
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    # HTTP request
    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
        # getting data in the json format
        data = response.json()
        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        temperature = int(temperature - 273.15)
        temp2 = main['feels_like']
        temp2 = int(temp2 - 273.15)
        # getting the humidity
        humidity = main['humidity']
        #description = main['description']
        return (temperature, humidity, temp2)
    else:
        # showing the error message
        return(0)

def locate():
    return(geo_data['city'], geo_data['region'], geo_data['country'])
