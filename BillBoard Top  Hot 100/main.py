import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year you would like to travel to? Enter date in format YYY-MM-DD: ")

URL = "https://www.billboard.com/charts/hot-100/2011-08-12/"

CLIENT_ID="b3c4a40816434643a85a427dbcade7b9"
CLIENT_SECRET ="340a06286d77473794d8983c0a25bf66"

response = requests.get(URL)
billboard_url = response.text

soup = BeautifulSoup(billboard_url, "html.parser")
song_titles = soup.select("li ul li h3")
song_name = [song.getText().strip() for song in song_titles]
print(song_name)

# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri="https://nich.org",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
    )
)
user_id = sp.current_user()["id"]
print(user_id)

# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]
for song in song_name:
    result = sp.search(q=f"track:{song} year: {year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

#A dding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)