import requests
from datetime import datetime
from config import AMADEUS_API_KEY, AMADEUS_SECRET

def get_amadeus_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "client_id": AMADEUS_API_KEY,
        "client_secret": AMADEUS_SECRET
    }
    response = requests.post(url, data=data, headers=headers)
    response.raise_for_status()
    return response.json()["access_token"]

def get_iata_code(city_name, token):
    url = f"https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword={city_name}&page[limit]=1"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    data = response.json()["data"]
    if not data:
        return None
    return data[0]["iataCode"]

def check_flight(origin_iata, dest_iata, token, is_direct=True):
    non_stop = "true" if is_direct else "false"
    today = datetime.today().strftime("%Y-%m-%d")
    url = (
        f"https://test.api.amadeus.com/v2/shopping/flight-offers?"
        f"originLocationCode={origin_iata}&destinationLocationCode={dest_iata}&"
        f"departureDate={today}&adults=1&nonStop={non_stop}&max=1"
    )
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = response.json()
    if "data" not in data or not data["data"]:
        return None
    flight = data["data"][0]
    price = float(flight["price"]["total"])
    segments = flight["itineraries"][0]["segments"]
    stops = len(segments) - 1
    final_destination = segments[-1]["arrival"]["iataCode"]
    return {"price": price, "stops": stops, "final_destination": final_destination}
