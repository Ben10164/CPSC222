import json
import requests

# we need a key, from, and to
# https://developer.mapquest.com/documentation/directions-api/route/get/

api_key = "INSERT KEY"
url = "http://www.mapquestapi.com/directions/v2/route"
url += "?key=" + api_key
url += "&from=spokane"
url += "&to=seattle"
print(url)

response = requests.get(url=url)

json_object = json.loads(response.text)

route_array = json_object["route"]

print("Distance:", route_array["distance"])

print("Time:", route_array["formattedTime"])
