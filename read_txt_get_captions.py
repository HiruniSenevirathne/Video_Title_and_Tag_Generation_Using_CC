import os
from video_id_to_json import yt_video_data


video_links_txt_file="./data_in/dataSet_info_1.txt"
json_folder_path='./out/'

def read_video_links_text_file():
    with open(video_links_txt_file) as f:
        lines=f.readlines()
        for line in lines:
            line=line.strip()
            if len(line)>1 & line.startswith('#')==False:
                
                # print(line)
                if os.path.isfile(json_folder_path+"video_info_"+line+".json")==False:
                    
                    print("Video Id is  processing",line)
                    yt_video_data(line)
                    print("Done")
                else:
                    print("Video Id is already proceed",line)
read_video_links_text_file()