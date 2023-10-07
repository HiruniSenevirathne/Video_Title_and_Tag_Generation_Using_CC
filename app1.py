# from googleapiclient.discovery import build

# # Set up the API client
# api_key = 'AIzaSyBFjuJoXZNu_6Bgd7Qd89svk9-gFH3-v9g'
# scopes = ['https://www.googleapis.com/auth/youtube.force-ssl',
# 'https://www.googleapis.com/auth/youtubepartner']
# youtube = build('youtube', 'v3', developerKey=api_key, scopes=scopes)

# # Send API request to retrieve the channel ID
# channel_name = 'Nadeemal Perera'  # Replace with the actual channel name
# # request = youtube.channels().list(
# #     part='id',
# #     forUsername=channel_name
# # )
# # request = youtube.captions().list(

# #     part='snippet',
# #     videoId='p6X_5rkkA-I'
# # )
# request = youtube.captions().download(

#     # videoId='p6X_5rkkA-I'
#     id='AUieDaaDmu5S3018vYeQz0ud1uyAxRYelhuZhrxlKViQz8GG2JI-I'
# )
# response = request.execute()
# print(response)

# # Extract the Channel ID from the API response
# channel_id = response['items'][0]['id']

# # print(f"The Channel ID for {channel_name} is: {channel_id}")

from googleapiclient.discovery import build

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'AIzaSyBFjuJoXZNu_6Bgd7Qd89svk9-gFH3-v9g'
youtube = build('youtube', 'v3', developerKey=api_key)

# Fetch trending videos
trending_videos = youtube.videos().list(part='snippet', chart='mostPopular', regionCode='US').execute()

for video in trending_videos['items']:
    print(video['snippet']['title'])
