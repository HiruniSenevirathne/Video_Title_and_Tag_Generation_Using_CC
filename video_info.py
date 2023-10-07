from googleapiclient.discovery import build
from google.auth import credentials
import json

# Set up the API client
api_key = 'AIzaSyBFjuJoXZNu_6Bgd7Qd89svk9-gFH3-v9g'
api_service_name = 'youtube'
api_version = 'v3'

youtube = build(api_service_name, api_version, developerKey=api_key)

def yt_get_video_info(video_id:str):
    
    response = youtube.videos().list(part='snippet', id=video_id).execute()
    # print(response)
    if 'items' in response:
        video = response['items'][0]
        title = video['snippet']['title']
        description=video['snippet']['description']
        tags=video['snippet']['tags']
        channel = video['snippet']['channelTitle']
        published_at = video['snippet']['publishedAt']

        # print("Title:", title)
        # print("Channel:", channel)
        # print("Published At:", published_at)
        # Serializing json
        # json_object = json.dumps(response, indent=4)
        
        # Writing to sample.json
        # with open("video_info.json", "w") as outfile:
        #     outfile.write(json_object)
        
        return title,description,tags,channel,published_at
    else:
        print("Video not found.")
        return None