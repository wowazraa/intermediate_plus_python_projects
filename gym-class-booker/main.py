import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

load_dotenv()

URL = "https://appbrewery.github.io/gym/"
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

wait = WebDriverWait(driver, 5)

# ------------------------------------ LOG IN ------------------------------------ #

join = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="home-page"]/section[1]/div/div/a[1]/button')))
join.click()

email = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]')))
email.send_keys(EMAIL)

password = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password-input"]')))
password.send_keys(PASSWORD)

login = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="submit-button"]')))
login.click()

# ---------------------------------- BOOK CLASS ---------------------------------- #

booked_count = 0
waitlist_count = 0
already_booked_count = 0
processed_classes = []

days = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[starts-with(@id, "day-title-")]')))
classes =["spin", "yoga", "hiit"]

for day in days:
    day_text = day.text.split(",")

    if day_text[0] == "Tue":
        date_ = day_text[1].split(" ")[2]
        date = f"0{date_}"

        for class_ in classes:
            slots = wait.until(EC.presence_of_all_elements_located((By.XPATH, f"//*[starts-with(@id, 'class-time-{class_}-2025-09-{date}-')]")))
            for slot in slots:

                slot_text1 = slot.text.split(" ")[1]
                slot_text2 = slot.text.split(" ")[2]

                if slot_text2 == "PM":
                    hour = str(int(slot_text1.split(":")[0]) + 12)
                else:
                    hour = slot_text1.split(":")[0]

                minu = slot_text1.split(":")[1]
                time = f"{hour}{minu}"

                if time == "1800":
                    button = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="book-button-{class_}-2025-09-{date}-{time}"]')))
                    button.click()

                    class_info = f"{class_} Class on {day_text[0]},{day_text[1]}"

                    if button.text == "Booked":
                        print(f"✓ Already booked: {class_info}")
                        already_booked_count += 1
                        processed_classes.append(f"[Booked] {class_info}")
                    elif button.text == "Waitlisted":
                        print(f"✓ Already on waitlist: {class_info}")
                        already_booked_count += 1
                        processed_classes.append(f"[Waitlisted] {class_info}")
                    elif button.text == "Book Class":
                        button.click()
                        print(f"✓ Successfully booked: {class_info}")
                        booked_count += 1
                        processed_classes.append(f"[New Booking] {class_info}")
                    elif button.text == "Join Waitlist":
                        button.click()
                        print(f"✓ Joined waitlist for: {class_info}")
                        waitlist_count += 1
                        processed_classes.append(f"[New Waitlist] {class_info}")

total_booked = already_booked_count + booked_count + waitlist_count

# ---------------------------------- CHECKINGS ---------------------------------- #

my_bookings_link = driver.find_element(By.ID, "my-bookings-link")
my_bookings_link.click()

wait.until(EC.presence_of_element_located((By.ID, "my-bookings-page")))

verified_count = 0

all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")

for card in all_cards:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text

        if ("Tue" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"✓ Verified: {class_name}")
            verified_count += 1

print("\n--- BOOKING SUMMARY ---")
print(f"Classes booked: {booked_count}")
print(f"Waitlists joined: {waitlist_count}")
print(f"Already booked/waitlisted: {already_booked_count}")
print(f"Total Tuesday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}")

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

logout = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="logout-button"]')))
logout.click()

driver.quit()












