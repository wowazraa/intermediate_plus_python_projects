from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 OPR/120.0.0.0",
    "Accept-Language": "tr,en-US;q=0.9,en;q=0.8,fr;q=0.7",
}

response = requests.get(url, headers=header)
soup = BeautifulSoup(response.content, "html.parser")
# print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]

price_as_float = float(price_without_currency)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

message = f"{title} is on sale for {price}!"
with smtplib.SMTP(os.environ["SMTP_ADDRESS"], port=587) as connection:
    connection.starttls()
    result = connection.login(os.environ["EMAIL_ADDRESS"], os.environ["EMAIL_PASSWORD"])
    connection.sendmail(
        from_addr=os.environ["EMAIL_ADDRESS"],
        to_addrs=os.environ["EMAIL_ADDRESS"],
        msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
    )
