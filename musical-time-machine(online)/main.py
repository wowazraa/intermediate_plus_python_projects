import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os
from datetime import datetime, timedelta

date_input = input("Which year do you want to travel to (1958-2021)? Type the date in this format YYYY-MM-DD: ")
date = datetime.strptime(date_input, "%Y-%m-%d")

valid_dates_url = "https://raw.githubusercontent.com/mhollingshead/billboard-hot-100/main/valid_dates.json"
response = requests.get(valid_dates_url)
valid_dates = [datetime.strptime(d, "%Y-%m-%d") for d in response.json()]

def nearest_saturday(date):
    delta_days = (5 - date.weekday()) % 7
    nearest = date + timedelta(days=delta_days)
    closest_date = min(valid_dates, key=lambda d: abs(d - nearest))
    return closest_date

week_date = nearest_saturday(date)
week_date_str = week_date.strftime("%Y-%m-%d")

URL = f"https://raw.githubusercontent.com/mhollingshead/billboard-hot-100/main/date/{week_date_str}.json"
response = requests.get(URL)

if response.status_code != 200:
    print(f"No Billboard Hot 100 data found for {week_date_str}.")
    exit()

try:
    chart_data = response.json()
except ValueError:
    print(f"Data for {week_date_str} is not valid JSON.")
    exit()

hot100_list = [(entry['song'], entry['artist']) for entry in chart_data.get('data', [])]

if not hot100_list:
    print(f"No songs found for {week_date_str}.")
    exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-private",
    cache_path=".cache-spotify"
))

user_id = sp.current_user()['id']

playlist_name = f"My Hot 100 {week_date_str} Playlist"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
print(f"Playlist created: {playlist_name}")

track_uris = []
for song, artist in hot100_list:
    result = sp.search(q=f"track:{song} artist:{artist}", type="track", limit=1)
    tracks = result['tracks']['items']

    if not tracks:
        result = sp.search(q=f"track:{song}", type="track", limit=1)
        tracks = result['tracks']['items']

    if tracks:
        track_uris.append(tracks[0]['uri'])
    else:
        print(f"Not found on Spotify: {song} - {artist}")

    time.sleep(0.5)

if track_uris:
    sp.playlist_add_items(playlist_id=playlist['id'], items=track_uris)
    print(f"Added {len(track_uris)} tracks to your playlist!")
else:
    print("No tracks found on Spotify to add.")
