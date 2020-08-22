

import spotipy.util as util
import pandas as pd
import time
import sys
import configparser
import os
import base64
import requests
import datetime
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from tabulate import tabulate
import spotipy

scope = "user-library-read playlist-modify-private"

OAuth = SpotifyOAuth(scope=scope,
        redirect_uri='http://localhost:8888/callback',
        client_id = 'client_id',
        client_secret = 'client_secret',
        username= 'username')
sp = spotipy.Spotify(auth_manager=OAuth)

# results = sp.current_user_saved_tracks()
# for idx, item in enumerate(results['items']):
#     track = item['track']
    # print(idx, track['artists'][0]['name'], " – ", track['name'])
# ----------------------------------

# def get_playlist_content():
#     offset = 0
#     songs = []
#     while True:
#         content = sp.current_user_saved_tracks(limit=50, offset=offset)
#         songs += content['items']
#         if content['next'] is not None:
#             offset += 50
#         else:
#             break
#     #
#     # with open('saved_tracks', 'w') as outfile:
#     #     json.dump(songs, outfile)
#
# def get_playlist_audio_features():
#     offset = 0
#     songs = []
#     items = []
#     ids = []
#     while True:
#         content = sp.current_user_saved_tracks(limit=50, offset=offset)

#         songs += content['items']
#         if content['next'] is not None:
#             offset += 100
#         else:
#             break
#
#     for i in songs:
#         ids.append(i['track']['id'])
#
#     index = 0
#     audio_features = []
#     while index < len(ids):
#         audio_features += sp.audio_features(ids[index:index + 50])
#         index += 50
#     features_list = []
#     for features in audio_features:
#         features_list.append([features['energy'], features['liveness'],
#                               features['tempo'], features['speechiness'],
#                               features['acousticness'], features['instrumentalness'],
#                               features['time_signature'], features['danceability'],
#                               features['key'], features['duration_ms'],
#                               features['loudness'], features['valence'],
#                               features['mode'], features['type'],
#                               features['uri']])
#
#     df = pd.DataFrame(features_list, columns=['energy', 'liveness',
#                                               'tempo', 'speechiness',
#                                               'acousticness', 'instrumentalness',
#                                               'time_signature', 'danceability',
#                                               'key', 'duration_ms', 'loudness',
#                                               'valence', 'mode', 'type', 'uri'])
#     print(tabulate(df,headers='firstrow'))
#     # df.to_csv('audio_features.csv', index=False)
#     print(df.columns)


# df = pd.read_csv("audio_features.csv")
# df["genre"] = ""
# print(tabulate(df[50:100], headers='keys', tablefmt='psql'))
#
# for index, row in df.iterrows():
#         uri = row['uri']
#         track = sp.track(uri)
#         artist_uri = track['album']['artists'][0]['uri']
#         artist = sp.artist(artist_uri)
#
#         genres = artist['genres']
#         str_genres = ' '.join([str(elem) for elem in genres])
#         row['genre'] = str_genres
#         df.loc[index, 'genre'] = row['genre']
#         # print(df.loc[index,'genre'])
#
#
# print(tabulate(df[50:100], headers='keys', tablefmt='psql'))
# df.to_csv('final_audio_features.csv', index=False)

playlist = sp.current_user_playlists()
print(playlist['items'][1]['id'])