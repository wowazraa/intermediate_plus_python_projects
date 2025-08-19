import requests
import os
from twilio.rest import Client

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/9c28b8e3a3d0a3989daf443af364a53d/flightDeals/prices"

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_API_SECRET = os.environ.get("AMADEUS_API_SECRET")

TWILIO_SID = os.environ.get("TWILIO_ACCOUNT_SID")
TWILIO_AUTH = os.environ.get("TWILIO_AUTH_TOKEN")
TWILIO_FROM = os.environ.get("TWILIO_FROM")
TWILIO_TO = os.environ.get("TWILIO_TO")

def get_amadeus_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_API_SECRET
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()["access_token"]

def get_sheet_data():
    response = requests.get(SHEETY_PRICES_ENDPOINT)
    response.raise_for_status()
    return response.json()["prices"]

def get_iata_code(city_name, token):
    url = f"https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword={city_name}&page[limit]=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()["data"]
    if not data:
        return None
    return data[0]["iataCode"]

def get_lowest_flight(origin_iata, dest_iata, token):
    url = f"https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode={origin_iata}&destinationLocationCode={dest_iata}&departureDate=2025-08-20&adults=1&max=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    if "data" not in data or not data["data"]:
        return None
    price = float(data["data"][0]["price"]["total"])
    date = data["data"][0]["itineraries"][0]["segments"][0]["departure"]["at"]
    return price, date

def update_sheet(city_id, iata, lowest_price):
    body = {
        "price": {
            "iataCode": iata,
            "lowestPrice": lowest_price
        }
    }
    url = f"{SHEETY_PRICES_ENDPOINT}/{city_id}"
    response = requests.put(url, json=body)
    response.raise_for_status()

def send_sms(message_text):
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages.create(
        body=message_text,
        from_=TWILIO_FROM,
        to=TWILIO_TO
    )
    print("SMS SENDED!")

def main():
    token = get_amadeus_token()
    sheet_data = get_sheet_data()
    origin_iata = "LHR"

    for city in sheet_data:
        city_name = city["city"]
        city_id = city["id"]
        current_iata = city.get("iataCode")
        lowest_price_recorded = city.get("lowestPrice", 0)

        if not current_iata:
            iata = get_iata_code(city_name, token)
            if iata:
                update_sheet(city_id, iata, lowest_price_recorded)
                current_iata = iata

        if current_iata:
            flight = get_lowest_flight(origin_iata, current_iata, token)
            if flight:
                price, date = flight
                if price < lowest_price_recorded or lowest_price_recorded == 0:
                    update_sheet(city_id, current_iata, price)
                    send_sms(f"{city_name} için yeni en ucuz uçuş: £{price} on {date}")

if __name__ == "__main__":
    main()
