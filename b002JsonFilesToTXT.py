import os
import json

links = []

for filename in os.listdir("./json/"):
    with open("./json/"+filename, 'r') as f: 
        data = json.load(f)
        for i in data.get("app_msg_list"):
            links.append(i["link"])

f = open("URLs.txt", "w")

for link in links:
    f.write(link)
    f.write("\n")

f.close()
