import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
import os

date_input = input("Which year do you want to travel to (1958-2025)? Type YYYY-MM-DD: ")
date = pd.to_datetime(date_input)

def select_file(date):
    if pd.to_datetime("1963-08-14") <= date <= pd.to_datetime("1967-10-18"):
        return "datas/billboard200.csv", "Billboard 200"
    elif pd.to_datetime("2004-10-27") <= date <= pd.to_datetime("2025-08-27"):
        return "datas/digital_songs.csv", "Digital Songs"
    elif pd.to_datetime("1958-08-06") <= date <= pd.to_datetime("1965-12-29"):
        return "datas/hot100.csv", "Hot 100"
    elif pd.to_datetime("1990-10-31") <= date <= pd.to_datetime("2025-08-27"):
        return "datas/radio.csv", "Radio"
    elif pd.to_datetime("2013-01-23") <= date <= pd.to_datetime("2025-08-27"):
        return "datas/streaming_songs.csv", "Streaming Songs"
    else:
        return None, None

file_name, chart_name = select_file(date)
if not file_name:
    print("Sorry, no data available for this date.")
    exit()

df = pd.read_csv(file_name)
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df = df.dropna(subset=['Date'])

df['delta'] = (df['Date'] - date).abs()
closest_week = df.loc[df['delta'].idxmin()]
week_date = closest_week['Date']

week_songs = df[df['Date'] == week_date]
hot100_list = list(zip(week_songs['Song'], week_songs['Artist']))

print(f"Using data from week: {week_date.date()} ({chart_name})")
print(f"Found {len(hot100_list)} songs.")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ.get("SPOTIFY_CLIENT_ID"),
    client_secret=os.environ.get("SPOTIFY_CLIENT_SECRET"),
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-modify-private",
    cache_path=".cache-spotify"
))

user_id = sp.current_user()['id']

playlist_name = f"Most Popular Songs of {week_date.date()}"
playlist = sp.user_playlist_create(user_id, name=playlist_name, public=False)
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

    time.sleep(0.2)

if track_uris:
    sp.playlist_add_items(playlist['id'], track_uris)
    print(f"Added {len(track_uris)} tracks to your playlist!")
else:
    print("No tracks found on Spotify to add.")
