from googleapiclient.discovery import build
from google.auth import credentials
import json

# Set up the API client
api_key = 'AIzaSyBFjuJoXZNu_6Bgd7Qd89svk9-gFH3-v9g'
api_service_name = 'youtube'
api_version = 'v3'


video_id="qgHeCfMa39E"
youtube = build(api_service_name, api_version, developerKey=api_key)
response = youtube.captions().list(part='snippet', videoId=video_id).execute()

if 'items' in response:
    for item in response['items']:

        if item['snippet']['language']=='en':

            print("Caption id:", item['id'])
else:
    print("Video not found.")