# Flight Deals Finder

A Python-based project that searches for the cheapest flight deals using the Amadeus API and stores/retrieves data from Google Sheets through Sheety API.
It also sends email notifications to subscribed users whenever a cheaper flight is found.

# Environment Variables

Create a .env file in the project root with the following values:


SHEETY_USERNAME=your_username
SHEETY_PASSWORD=your_password
SHEETY_PRICES_ENDPOINT=https://api.sheety.co/.../prices
SHEETY_USERS_ENDPOINT=https://api.sheety.co/.../users

AMADEUS_API_KEY=your_amadeus_api_key
AMADEUS_SECRET=your_amadeus_secret


EMAIL_ADDRESS=your_email@example.com
EMAIL_PASSWORD=your_email_password
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587

Important: If you use Gmail, make sure to enable App Passwords instead of your regular password.


# Example Email

Subject: New Flight Deal!
Body:

New flight deal!
LHR -> JFK for GBP 320 (direct)
