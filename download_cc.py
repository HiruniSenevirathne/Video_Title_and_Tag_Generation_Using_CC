from youtube_transcript_api import YouTubeTranscriptApi

# assigning srt variable with the list of dictionaries
# obtained by the .get_transcript() function
# and this time it gets only the subtitles that
# are of english language.
def yt_get_captions(video_id:str):

    captionsList = YouTubeTranscriptApi.get_transcript(video_id,
                                            languages=['en'])
    ccStr = ''

    for item in captionsList:
        ccStr = ccStr + '. '+item['text']
        
    return ccStr

    # with open("video_transcript.txt", "w") as outfile:
    #         outfile.write(ccStr)