# Musical Time Machine (Online Version)

This project lets you travel back in time musically by creating a Spotify playlist with the **Billboard Hot 100** songs from a specific date.  
Unlike the offline version, this script fetches chart data **directly from GitHub (live JSON files)**.

---

## Features
-  Input any date between **1958-2021** (`YYYY-MM-DD` format).
-  Automatically finds the **nearest Saturday chart** (Billboard charts are published weekly).
-  Fetches Billboard Hot 100 data **online** from [mhollingshead/billboard-hot-100](https://github.com/mhollingshead/billboard-hot-100).
-  Creates a private Spotify playlist with all songs from that chart.
-  Uses the Spotify API to search for songs and build playlists.

---

## Requirements
- Python 3.8+
- [requests](https://pypi.org/project/requests/)
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
  cd intermediate_plus_python_projects/musical-time-machine(online)
```
2. Install dependencies:
  ```
  pip install requests spotipy
  ```
3. Create a .env file (or set environment variables) with your Spotify credentials:
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
  Which year do you want to travel to (1958-2021)? Type the date in this format YYYY-MM-DD:
  ```
The program finds the nearest valid Billboard Saturday date.

Downloads chart data (JSON) from GitHub.

Creates a private Spotify playlist with the found songs.

---

### Notes
If a song cannot be found on Spotify, it is skipped (with a console warning).

Billboard Hot 100 data is fetched from GitHub, so an internet connection is required.

This online version always uses the most up-to-date Billboard chart archive.
