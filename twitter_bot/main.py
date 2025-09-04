import os
import time
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

PROMISED_DOWN = 35
PROMISED_UP = 10
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASS = os.environ.get("TWITTER_PASS")

URL_SPEEDTEST = "https://www.speedtest.net/"
URL_TWITTER = "https://x.com/i/flow/login?lang=trmai"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.down = 0
        self.up = 0
        self.text = ""

    def get_internet_speed(self):
        self.driver.get(URL_SPEEDTEST)

        wait = WebDriverWait(self.driver, 10)

        try:
            accept_button = wait.until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
            accept_button.click()
        except:
            print("Cookie banner bulunamadı, devam ediliyor...")

        go_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[2]/a/span[4]')))
        go_button.click()

        time.sleep(60)

        down_web = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')))
        self.down = down_web.text

        up_web = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')))
        self.up = up_web.text

        self.text = f"Hey IP, why my internet speed {self.down}down/{self.up} when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"

        print(f"down: {self.down}")
        print(f"up: {self.up}")


    def tweet_at_provider(self):
        self.driver.get(URL_TWITTER)
        wait = WebDriverWait(self.driver, 15)

        google_login = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//span[text()="Google ile oturum açın"]/ancestor::div[@role="button"]'))
        )
        google_login.click()

        self.driver.switch_to.window(self.driver.window_handles[-1])

        email_box = wait.until(EC.presence_of_element_located((By.ID, "identifierId")))
        email_box.send_keys(TWITTER_EMAIL)
        email_box.send_keys(Keys.ENTER)

        time.sleep(3)

        next_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierNext"]/div/button/div[3]')))
        next_button.click()
        
        time.sleep(3)

        password_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        password_box.send_keys(TWITTER_PASS)
        password_box.send_keys(Keys.ENTER)

        self.driver.switch_to.window(self.driver.window_handles[0])

        time.sleep(5)

        tweet_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[role="textbox"]')))
        tweet_box.send_keys(self.text)

        post_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@data-testid="tweetButtonInline"]')))
        post_button.click()

        print("Tweet sended!")

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()


