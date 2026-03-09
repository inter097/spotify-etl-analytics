import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-top-read"
))

canciones = []

for periodo in ["short_term", "medium_term", "long_term"]:
    result = sp.current_user_top_tracks(limit=50, time_range=periodo)
    for item in result["items"]:
        canciones.append({
            "cancion": item["name"],
            "artista": item["artists"][0]["name"],
            "album": item["album"]["name"],
            "popularidad": item.get("popularity", 0),
            "fecha_extraccion": pd.Timestamp.today().date(),
            "fuente": periodo
        })

df = pd.DataFrame(canciones)
df.to_csv("spotify_raw.csv", index=False)
print(df)
print(f"\nTotal registros: {len(df)}")
print("✅ CSV guardado!")