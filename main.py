import requests
from twilio.rest import Client
api_key = "your api_key"
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
long = 100.501762
lat = 13.756331
cnt = 4
account_sid = "your_account_sid"
auth_token = "your auth_token"


weather_params = {
    "lat": lat,
    "lon": long,
    "cnt": cnt,
    "appid": api_key
}
# https://api.openweathermap.org/data/2.5/weather?q=London,UK&appid=fabe7bd041f714c888c1611434b7edb1

# https://api.openweathermap.org/data/2.5/forecast?lat=77.706413&lon=28.984463&appid=fabe7bd041f714c888c1611434b7edb1


response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="twilio mobile number",
        body="It's going to rain today. Remember to bring an '☔️'",
        to="your registered mobile number" #+91XXXXXXXXXXX
    )

  print(message.status)


