import requests
import json
import test_spotify 

# Shazam API request
shazam_url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"
shazam_files = {"upload_file": open('wedding_dance.mp3', 'rb')}
shazam_headers = {
    "X-RapidAPI-Key": "bb18a2b436mshe73c2ca9f99ebedp11e5e5jsn70caa4cb3bca",
    "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
}

shazam_response = requests.post(shazam_url, files=shazam_files, headers=shazam_headers)
shazam_data = shazam_response.json()
json_formatted_str = json.dumps(shazam_response.json(), indent=2)
# print(json_formatted_str)
# print(response.json())

# Extracting track details from Shazam response
shazam_track = shazam_data.get('track', {})
shazam_title = shazam_track.get('title', '')
shazam_artist = shazam_track.get('subtitle', '')
# print (shazam_track)
print (shazam_title)
print (shazam_artist)


test_spotify.search_spotify(shazam_title,shazam_artist)
# # Spotify API request
# spotify_url = f"https://spotify23.p.rapidapi.com/search?q={shazam_title} {shazam_artist}&type=track&limit=1"
# spotify_headers = {
#     'X-RapidAPI-Key': "bb18a2b436mshe73c2ca9f99ebedp11e5e5jsn70caa4cb3bca",
#     'X-RapidAPI-Host': "spotify23.p.rapidapi.com"
# }

# spotify_response = requests.get(spotify_url, headers=spotify_headers)
# spotify_data = spotify_response.json()

# # Extract Spotify ID from the Spotify API response
# spotify_track_id = spotify_data.get('tracks', {}).get('items', [{}])[0].get('id', '')

# print(f"Spotify Track ID: {spotify_track_id}")













# import asyncio
# from shazamio import Shazam
# import json

# async def main():
#   shazam = Shazam()
#   # out = await shazam.recognize_song('dora.ogg') # slow and deprecated, don't use this!
#   out = await shazam.recognize('wedding_dance.mp3')  # rust version, use this!
  
# #   json_object = json.loads(out['matches'])
#   json_formatted_str = json.dumps(out, indent=2)
# #   print(json_formatted_str)
#   print(out['track']['title'])
# #   print(type(out['matches']))

# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())