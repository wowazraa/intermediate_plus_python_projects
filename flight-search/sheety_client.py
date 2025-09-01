import requests
from config import SHEETY_AUTH, SHEETY_PRICES_ENDPOINT, SHEETY_USERS_ENDPOINT

def get_sheet_data(endpoint):
    response = requests.get(endpoint, auth=SHEETY_AUTH)
    response.raise_for_status()
    return response.json()

def update_sheet(city_id, iata=None, lowest_price=None):
    update_data = {"price": {}}
    if iata:
        update_data["price"]["iataCode"] = iata
    if lowest_price:
        update_data["price"]["lowestPrice"] = lowest_price
    response = requests.put(f"{SHEETY_PRICES_ENDPOINT}/{city_id}", json=update_data, auth=SHEETY_AUTH)
    return response.json()

def get_customer_emails():
    data = get_sheet_data(SHEETY_USERS_ENDPOINT)
    users = data.get("users", [])
    emails = []
    for user in users:
        for key in user.keys():
            if "email" in key.lower():
                emails.append(user[key])
    return emails
