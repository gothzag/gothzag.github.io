import spotipy
from spotipy import Spotify as sp
import spotipy.oauth2 as oauth2
from spotipy.oauth2 import SpotifyClientCredentials
import time

# your client id and secret are obtained by creating an app on https://developer.spotify.com/dashboard/applications

# ensure that you have added `http://google.com/` as the redirect URI for your app on developer.spotipy.com

client_id = 'YOUR_CLIENT_ID'
client_secret = 'YOUR_CLIENT_SECRET'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def getTrackIDs(user, playlist_id):
    ids = []
    playlist = sp.user_playlist(user, playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    return ids
    
ids = getTrackIDs('YOUR_USER_ID', 'YOUR_PLAYLIST_ID')

def getTrackFeatures(id):
  meta = sp.track(id)
  features = sp.audio_features(id)

  # metadata
  name = meta['name']

  # audio features
  acousticness = features[0]['acousticness']
  danceability = features[0]['danceability']
  energy = features[0]['energy']
  instrumentalness = features[0]['instrumentalness']
  liveness = features[0]['liveness']
  valence = features[0]['valence']
  tempo = features[0]['tempo']

  track = [name, danceability, acousticness, danceability, energy, instrumentalness, liveness, valence, tempo]
  return track

  # track ids loop
tracks = []
for i in range(len(ids)):
  time.sleep(.5)
  track = getTrackFeatures(ids[i])
  tracks.append(track)

  # create dataset
df = pd.DataFrame(tracks, columns = ['name', 'danceability', 'acousticness', 'danceability', 'energy', 'instrumentalness', 'liveness', 'valence', 'tempo'])
df.to_csv("spotify.csv", sep = ',')
