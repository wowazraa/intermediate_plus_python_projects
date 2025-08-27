# Flight Search Project ✈️

This project searches for cheap flights using the Amadeus API and notifies users via email.  
It integrates with Google Sheets through the Sheety API to manage destinations and users.  

## Features
- Fetches flight deals from the Amadeus API  
- Stores and retrieves data from Google Sheets using Sheety  
- Sends email notifications to users when deals are found  
- Secure API keys and credentials with `.env` file

## Environment Variables

Create a `.env` file in the project root with the following content:

```env
SHEETY_USERNAME= 
SHEETY_PASSWORD= 
SHEETY_PRICES_ENDPOINT= 
SHEETY_USERS_ENDPOINT= 
SHEETY_AUTH= 

AMADEUS_API_KEY= 
AMADEUS_SECRET= 

EMAIL_ADDRESS= 
EMAIL_PASSWORD= 
SMTP_SERVER= 
SMTP_PORT= 
```
⚠️ Do not share your .env file publicly.

## Notes

The Amadeus API requires you to create an account and get test credentials.

Sheety API requires you to connect your Google Sheet.

Emails are sent using Gmail SMTP (enable "App Passwords" or "Less secure apps" depending on your Gmail settings).
