import requests

apiKey = "547ee1495b18999b528ff3fd1b3faf0f"
apiToken = {"apikey": apiKey}
url = "http://api.openweathermap.org/data/2.5/weather"
query_params1 = {"q": "hyderabad", "appid": apiKey}


def get_current_weather_details():
    response = requests.get(url, headers=apiToken, params=query_params1)
    return response.json()


def get_weather_details_from_long_lat():
    query_params2 = {"lat": get_current_weather_details()["coord"]["lat"],
                     "lon": get_current_weather_details()["coord"]["lon"], "appid": apiKey}
    r = requests.get(url, headers=apiToken, params=query_params2)
    body = r.json()
    assert body["name"] == "Hyderabad" and body["sys"]["country"] == "IN"
    assert body["main"]["temp_min"] > 0 and body["main"]["temp"] > 0


get_current_weather_details()
get_weather_details_from_long_lat()