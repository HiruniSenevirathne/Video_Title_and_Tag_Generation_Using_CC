import pandas as pd
import json
import os

dataset_dir="./out"
data_files=os.listdir(dataset_dir)

print(data_files)

data_points=[]

for file_name in data_files:
    if file_name.endswith('.json'):
        with open(dataset_dir+"/"+file_name) as f:
            json_data = json.load(f)
            # print(json_data['title'])
            data_points.append(json_data)
        
        
df = pd.DataFrame(data_points)
print(df.head())
df.to_csv('./out/points.csv')
        
# # Reading JSON data from a file
# with open("data.json") as f:
#     json_data = json.load(f)

# # Converting JSON data to a pandas DataFrame
# df = pd.read_json(json_data)
# # Writing DataFrame to a CSV file
# df.to_csv("output.csv", index=False)