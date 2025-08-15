import requests
import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_key = "95b2377a6825f07f200fba84c92305c7"

weather_params = {
    "appid": API_key,
    "lat": 11.09596000,
    "lon": 11.33261000,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]

    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        from_=from_number,
        to="+905510139029",
    )
    print(message.status)
