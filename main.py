import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("Twilio_SID")
auth_token = os.environ.get("Twilio_Auth")
parameters = {"lat": 4.771490, "lon": 7.014350, "appid": os.environ.get("OWM_Token"), "cnt":4,}
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params= parameters)
response.raise_for_status()
weather = response.json()
weather_codes = []
will_rain = False

for item in weather["list"]:
    new_code = item["weather"][0]["id"]
    if int(new_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages .create(
    body='It will rain today. Remember to bring an umbrella!',
    from_='+16066490168',
    to='+2349078168088'
    )

    print(message.status)
