from datetime import date
import json
import pandas as pd
import numpy as np

import requests
from requests.models import Response


# we need a key, from, and to
# https://developer.mapquest.com/documentation/directions-api/route/get/

def get_lat_lon(location):
    api_key = "UAnT0niwKTi1x0mUHDKqU6XIi2WxDNxZ"
    url = "http://open.mapquestapi.com/geocoding/v1/address"
    url += "?key=" + api_key
    url += "&location=" + location

    response = requests.get(url=url)
    json_object = json.loads(response.text)

    results_array = json_object["results"]

    locations_array = results_array[0]
    main_location = locations_array['locations']
    latLng = main_location[0]['latLng']
    lat = latLng['lat']
    lng = latLng['lng']

    # or a more simplified way to do it
    # lat = results_array[0]['locations'][0]['latLng']['lat']
    # lng = results_array[0]['locations'][0]['latLng']['lng']

    return lat, lng


def get_weather_station(lat, lon):
    url = "https://meteostat.p.rapidapi.com/stations/nearby"

    headers = {
        'x-rapidapi-host': "meteostat.p.rapidapi.com",
        'x-rapidapi-key': "179c1299a0mshafe5eb652712c44p17f1f6jsn7969744af56d"
    }
    url += "?lat=" + str(lat)
    url += "&lon=" + str(lon)

    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    data = results['data']
    first_result_id = data[0]['id']

    return first_result_id


def get_weather_data(station):
    # https: // meteostat.p.rapidapi.com/stations/daily?station = 10637 & start = 2020-01-01 & end = 2020-01-31'
    url = "https://meteostat.p.rapidapi.com/stations/daily"
    url += "?station=" + station

    url += "&start=2021-01-01"
    today = date.today()
    url += "&end=" + today.strftime("%Y")+"-"+today.strftime("%m") + \
        "-" + today.strftime("%d")  # today.strftime("%Y%m%d/")
    url += "&units=imperial"
    print(url)

    headers = {
        'x-rapidapi-host': "meteostat.p.rapidapi.com",
        'x-rapidapi-key': "179c1299a0mshafe5eb652712c44p17f1f6jsn7969744af56d"
    }

    response = requests.get(url, headers=headers)
    results = json.loads(response.text)
    df = pd.json_normalize(results)
    return pd.DataFrame(df['data'][0])


# city = input(
#     "What city do you want to see? (if there are spaces replace them with a +) ")
city = "seattle"
lat, lon = get_lat_lon(city)

print("Fun fact! Did you know the latitude of your city is",
      lat, "and the longitude is", lon, "? Well now you do!")

weather_station = get_weather_station(lat, lon)

print("The closest weather station to that location is station", weather_station)

df = get_weather_data(weather_station)

# before cleaning
filename = ""+city+"_daily_weather"
df.to_csv(filename+".csv")

# cleaning
df.replace("null", np.NaN, inplace=True)

cols_to_drop = []

for col in df.columns:
    ser = df[col]
    if ser.isnull().sum() > (ser.size * 0.75):
        cols_to_drop.append(col)

df = df.drop(columns=cols_to_drop)


df = df.interpolate(method='linear')
df = df.fillna(method='bfill')
df = df.fillna(method='ffill')

df = df.set_index('date')


# after cleaning
filename += "_cleaned"
df.to_csv(filename+".csv")
