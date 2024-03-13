import requests
import json
from . import spotify 

def get_spotifyID(file_name):
    # Shazam API request
    shazam_url = "https://shazam-api-free.p.rapidapi.com/shazam/recognize/"
    shazam_files = {"upload_file": open('/Users/sara/Desktop/test_song.mp3', 'rb')}
    print('file uploaded')
    shazam_headers = {
        "X-RapidAPI-Key": "bb18a2b436mshe73c2ca9f99ebedp11e5e5jsn70caa4cb3bca",
        "X-RapidAPI-Host": "shazam-api-free.p.rapidapi.com"
    }

    shazam_response = requests.post(shazam_url, files=shazam_files, headers=shazam_headers)
    shazam_data = shazam_response.json()
    # json_formatted_str = json.dumps(shazam_response.json(), indent=2)
    # print(json_formatted_str)
    # print(response.json())

    # Extracting track details from Shazam response
    shazam_track = shazam_data.get('track', {})
    shazam_title = shazam_track.get('title', '')
    shazam_artist = shazam_track.get('subtitle', '')
    # print (shazam_track)
    print ('title:', shazam_title)
    print ('artist:',shazam_artist)


    return spotify.search_spotify(shazam_title,shazam_artist)