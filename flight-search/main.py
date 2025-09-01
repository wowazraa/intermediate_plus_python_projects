from amadeus_client import get_amadeus_token, get_iata_code, check_flight
from data_manager import SHEETY_PRICES_ENDPOINT, SHEETY_USERS_ENDPOINT, get_sheet_data, update_sheet, get_customer_emails
from notification_manager import send_emails

def main():
    token = get_amadeus_token()
    origin_iata = "LHR"

    sheet_data = get_sheet_data(SHEETY_PRICES_ENDPOINT).get("prices", [])

    for city in sheet_data:
        city_name = city["city"]
        city_id = city["id"]
        current_iata = city.get("iataCode")
        lowest_price_recorded = city.get("lowestPrice", 0)

        if not current_iata:
            iata = get_iata_code(city_name, token)
            if iata:
                current_iata = iata
                update_sheet(city_id, iata=current_iata)

        if current_iata:
            flight = check_flight(origin_iata, current_iata, token, is_direct=True)
            if not flight:
                flight = check_flight(origin_iata, current_iata, token, is_direct=False)

            if flight:
                price = flight["price"]
                stops = flight["stops"]
                final_dest = flight["final_destination"]

                if price < lowest_price_recorded or lowest_price_recorded == 0:
                    update_sheet(city_id, lowest_price=price)
                    emails = get_customer_emails()
                    stop_text = "direct" if stops == 0 else f"{stops} stop(s)"
                    message = f"New flight deal!\n{origin_iata} -> {final_dest} for GBP{price} ({stop_text})"
                    send_emails(emails, subject="New Flight Deal!", message=message)
                    print(f"Notification sent for {city_name}: GBP{price} ({stop_text})")

if __name__ == "__main__":
    main()
