import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://ozh.github.io/cookieclicker"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(5)

cookie = driver.find_element(By.ID, "bigCookie")

products = {
    10: "product10",
    9: "product9",
    8: "product8",
    7: "product7",
    6: "product6",
    5: "product5",
    4: "product4",
    3: "product3",
    2: "product2",
    1: "product1",
    0: "product0"
}

last_purchase = time.time()

while True:
    cookie.click()

    if time.time() - last_purchase > 10:
        cookies_text = driver.find_element(By.ID, "cookies").text.split(" ")[0]
        cookies_n = int(cookies_text.replace(",", ""))

        for i in range(10, -1, -1):
            try:
                product = driver.find_element(By.ID, products[i])
                classes = product.get_attribute("class")

                if "enabled" in classes:
                    product.click()
            except:
                continue

        last_purchase = time.time()
