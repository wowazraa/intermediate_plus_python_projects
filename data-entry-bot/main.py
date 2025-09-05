import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_Zillow = "https://appbrewery.github.io/Zillow-Clone"
URL_Drive = "https://docs.google.com/forms/d/1J8n_HI5JNznyJTxWNCvaCb4ZLMUAYIcjLKCoKm7EuEc/edit"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL_Drive)

wait = WebDriverWait(driver, 5)

response = requests.get(URL_Zillow)
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
list_of_apt = soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")

link_list = []
price_list = []
address_list = []

for apt in list_of_apt:
    apt_link= apt.find(name="a", class_="StyledPropertyCardDataArea-anchor")["href"]
    link_list.append(apt_link)

    apt_price = apt.find(name="span", class_="PropertyCardWrapper__StyledPriceLine").get_text(strip=True).split("+")[0]
    price_list.append(apt_price)

    apt_address = apt.find(name="address").get_text(strip=True).replace("\n", " ")
    address_list.append(apt_address)

    address_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    address_input.send_keys(apt_address)

    price_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    price_input.send_keys(apt_price)

    link_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
    link_input.send_keys(apt_link)

    submit = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')))
    submit.click()

    another_answer = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
    another_answer.click()

driver.quit()





