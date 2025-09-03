# Gym Class Booker

Automates booking gym classes on [App Brewery Gym](https://appbrewery.github.io/gym/) website using Selenium.

---

## Features

- Logs in using credentials stored in a `.env` file.
- Automatically checks for **Tuesday 6:00 PM classes**.
- Books available classes or joins waitlists if necessary.
- Verifies booked classes against the "My Bookings" page.
- Prints a summary of actions taken:
  - Classes booked
  - Waitlists joined
  - Already booked/waitlisted classes
  - Verification of processed classes

---

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/GymClassBooker.git
```
2. Create a virtual environment and activate it:

```
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```
3. Install dependencies:

```
pip install -r requirements.txt
```
4. Create a .env file in the project root with your credentials:

```
EMAIL=your_email@example.com
PASSWORD=your_password
```
---

## Usage
Run the script:

```
python main.py
```

---

#### The script will:

Open Chrome with a dedicated user profile (chrome_profile folder).

Log in with your credentials.

Book or waitlist Tuesday and Thursday 6:00 PM classes.

Verify bookings.

Print a booking summary and verification result.

Log out and close the browser.

---

## Notes
Chrome must be installed and compatible with the Selenium version used.

User profile data is stored in chrome_profile to preserve session preferences.

Make sure .env is included in .gitignore to protect credentials.
