# Musical Time Machine (Offline Version)

This project allows you to travel back in time musically by creating a Spotify playlist with the top Billboard songs from a specific date.  
It works **offline** by using local CSV files that contain Billboard Hot 100 data.

---

## Features
-  Input any date between **1958-2025** (`YYYY-MM-DD` format).
-  If the exact date does not exist in the dataset, it will automatically select the **closest available date**.
-  Reads Billboard Hot 100 charts from local CSV files stored in the `datas/` folder.
-  Creates a new Spotify playlist with the songs from that chart.
-  Uses the Spotify API for playlist creation and track search.

---

## Requirements
- Python 3.8+
- [pandas](https://pandas.pydata.org/)
- [spotipy](https://spotipy.readthedocs.io/)
- Spotify Developer account with:
  - **Client ID**
  - **Client Secret**
  - **Redirect URI**

---

## Installation
1. Clone this repository:
```
git clone https://github.com/YOUR-USERNAME/intermediate_plus_python_projects.git
cd intermediate_plus_python_projects/musical-time-machine(offline)
```
2. Install dependencies:
  ```
  pip install pandas spotipy
  ```
3. Place your Billboard CSV files inside:
  ```
  musical-time-machine(offline)/datas/
  ```
5. Create a .env file (or set environment variables) with your Spotify credentials:
  ```
  SPOTIPY_CLIENT_ID=your_client_id
  SPOTIPY_CLIENT_SECRET=your_client_secret
  SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
  ```

---

## Usage
Run the program:
  ```
  python main.py
  ```
You will be prompted to enter a date:
  ```
  Which year do you want to travel to (1958-2025)? Type YYYY-MM-DD:
  ```
If the exact date exists in datas/, that chart will be used.
If not, the script finds the closest available chart date.

A Spotify playlist will then be created with the corresponding songs.

---

### Notes
Some songs may not be available on Spotify.

Playlist creation requires you to log in via Spotify’s OAuth flow (browser opens automatically).

This offline version avoids web scraping by relying only on local CSV data.
