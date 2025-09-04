# Internet Speed Twitter Bot

This project is a Python bot that tests your internet speed and automatically tweets at your ISP if your speed is below the promised values. It also supports logging in to X (Twitter) via Google.

---

## Features

- Measures internet speed (Download / Upload)
- Compares results with your promised internet speed
- Logs in to X (Twitter) using Google account
- Automatically posts a tweet if speed is low

---

## Requirements

- Python 3.10+
- Google Chrome and compatible [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/)
- Python libraries:

```
pip install selenium python-dotenv
```

---

## Setup
Clone the repository:
```
git clone <repo-link>
cd <repo-folder>
```
Create a .env file and add your Google account credentials:
```
TWITTER_EMAIL=your_email@gmail.com
TWITTER_PASS=your_password
```
Optional: Create a chrome_profile folder in the project directory. The bot will use this folder to store Chrome profile data.

## Usage
```
from bot import InternetSpeedTwitterBot
```

---

### When running the bot:

- Chrome will open and perform a speed test on speedtest.net

- Logs in to X (Twitter) via your Google account

- Fills the tweet box and posts a tweet automatically

## Notes
The Google login process may sometimes require CAPTCHA or additional verification. In such cases, manual intervention is needed.

Ensure your ChromeDriver version matches your installed Chrome browser.

The bot stores Chrome profile data in the chrome_profile folder to maintain session cookies and avoid logging in every time.
