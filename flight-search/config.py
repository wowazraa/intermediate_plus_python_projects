import os
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
SHEETY_PASSWORD = os.environ.get("SHEETY_PASSWORD")
SHEETY_PRICES_ENDPOINT = os.environ.get("SHEETY_PRICES_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")
SHEETY_AUTH = HTTPBasicAuth(SHEETY_USERNAME, SHEETY_PASSWORD)

AMADEUS_API_KEY = os.environ.get("AMADEUS_API_KEY")
AMADEUS_SECRET = os.environ.get("AMADEUS_SECRET")

EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
