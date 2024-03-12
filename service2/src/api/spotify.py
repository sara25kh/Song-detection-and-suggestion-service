import requests

def search_spotify(title, artist):
    url = f"https://spotify23.p.rapidapi.com/search?q={title} {artist}&type=track&limit=1"
    headers = {
        'X-RapidAPI-Key': "bb18a2b436mshe73c2ca9f99ebedp11e5e5jsn70caa4cb3bca",
        'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    data = response.json()
    # print(data)

    # Extract Spotify ID from the Spotify API response
    spotify_track_id = data.get('tracks', {}).get('items', [{}])[0].get('data', {}).get('uri', '').split(':')[-1]


    return spotify_track_id

# Use the function in your code
shazam_title = "My Girl"  # Replace with the actual title from the Shazam response
shazam_artist = "Oskar Cyms"  # Replace with the actual artist from the Shazam response

spotify_track_id = search_spotify(shazam_title, shazam_artist)

print(f"Spotify Track ID: {spotify_track_id}")

def get_spotifyID(shazam_title, shazam_artist):
    spotify_track_id = search_spotify(shazam_title, shazam_artist)

    print(f"Spotify Track ID: {spotify_track_id}")