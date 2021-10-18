"""
Explanation of program

The goal of the program:

Be able to connect to the running Spotify account and extract current playing information. 
Be able to play a specific song based on input through Spotify.


Steps: 
Create a Spotify developer account: 
https://developer.spotify.com/dashboard/
Extract a Spotify API
Print output of current playing 
Play specific song based on input

Helpful Links/code
https://developer.spotify.com/console/get-users-currently-playing-track/
https://api.spotify.com/v1/me/player/currently-playing
response = requests.get(SPOTIFY_GET_CURRENT_TRACK_URL,headers={"Authorization": f"Bearer {ACCESS_TOKEN}"})
"""