import requests
import os
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token  = os.getenv("TWILIO_AUTH_TOKEN")
from_number = os.getenv("TWILIO_FROM")

NEWS_API_KEY = "4a85117c98c9485b8ebffc598ebbd9cc"
STOCK_API_KEY = "GMICM439C779SFNK"

STOCK = "UNH"
COMPANY_NAME = "UnitedHealth"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

stock_data = stock_response.json()["Time Series (Daily)"]
data_list = list(stock_data.items())

yesterday = float(data_list[0][1]["4. close"])
before_yesterday = float(data_list[1][1]["4. close"])

difference = yesterday - before_yesterday
diff_percent = 100 * abs(difference) / yesterday

if difference > 0:
    first_line = f"{STOCK}: 🔺{diff_percent}%"
else:
    first_line = f"{STOCK}: 🔻{diff_percent}%"

news_params = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

news_response = requests.get(NEWS_ENDPOINT, params=news_params)
news_response.raise_for_status()

articles = news_response.json()["articles"]
three_articles = articles[:3]

if diff_percent >= 5:
    client = Client(account_sid, auth_token)

    for article in three_articles:
        title = article["title"]
        content = article["content"]

        message = client.messages.create(
            body=f"{first_line}\nHeadline: {title}\nBrief: {content}\n\n",
            from_=from_number,
            to="+905510139029",
        )

        # for testing
        print(f"{first_line}\nHeadline: {title}\nBrief: {content}\n\n")
        print(message.sid)
