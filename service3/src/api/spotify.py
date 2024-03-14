import requests

def get_recommendations(spotify_track_id):
    url = "https://spotify23.p.rapidapi.com/recommendations/"

    querystring = {
        "limit": "3",
        "seed_tracks": spotify_track_id
    }

    headers = {
        "X-RapidAPI-Key": "bb18a2b436mshe73c2ca9f99ebedp11e5e5jsn70caa4cb3bca",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        json_data = response.json()
        
        # Extract track names and artists
        tracks_info = []
        for track in json_data['tracks']:
            track_info = [track['name'], track['artists'][0]['name']]
            tracks_info.append(track_info)
        
        return tracks_info
    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")

# trackID = '2tZ9SSCDM5uJS8ZXGdfvCf'
# recommendations = get_recommendations(trackID)
# print('recommendations:',recommendations)