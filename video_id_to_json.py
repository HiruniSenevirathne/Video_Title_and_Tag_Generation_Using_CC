import video_info
import download_cc
import json

def yt_video_data(video_id:str):
    title,description,tags,channel,published_at = video_info.yt_get_video_info(video_id)
    captions = download_cc.yt_get_captions(video_id)
    
    # print(title,description,tags,channel,published_at)
    # print(captions)
    
    response={
        'video_id':video_id, 
        'title':title,
        'description':description,
        'tags':tags,
        'channel':channel,
        'published_at':published_at,  
        'captions':captions, 
        'caption_length':len(captions),
        'caption_words_count':len(captions.split())
    }
    json_object = json.dumps(response, indent=4)
    with open("./out/video_info_"+video_id+".json", "w") as outfile:
        outfile.write(json_object)
        
# /yt_video_data("BpDBquq8g40")