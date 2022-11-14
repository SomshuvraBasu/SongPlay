#code to fetch all videos url in a playlist

import urllib.request
import re
# import os

url="https://youtube.com/playlist?list=PLc8Z2v5RjCNGNavkJbqBCHKiyK2Ijw4W4"

def get_video_ids(url):
    html = urllib.request.urlopen(url).read().decode('utf-8')
    video_ids = re.findall(r"watch\?v=(\S{11})", html)
    return video_ids

def get_video_title(url):
    html = urllib.request.urlopen(url).read().decode('utf-8')
    video_title = re.findall(r"<title>(.+?)</title>", html)
    return video_title


idList=get_video_ids(url)

#create a dictionary to store video ids as keys and video titles as values
idDict={}
for id in idList:
    if id not in idDict:
        title=get_video_title("https://www.youtube.com/watch?v="+id)[0]
        idDict[id]=title[0:15]    

print(idDict)

#delete duplicate video ids as first video of playlist appears multiple times
idList=list(idDict.keys())

#check if play.csv is empty
# if os.stat("play.csv").st_size == 0:
#     flag=False
# else:
#     flag=True

# to avoid comma at first id in csv file
flag=False

with open("play.csv", "w+") as f:
    for i in range(len(idList)):
        video_id=idList[i]
        if(flag==False):
            f.write("'"+video_id+"'")
            flag=True
        else:
            f.write(", '"+video_id+"'")

# read play.csv as a list removing quotes and spliting by comma
# with open("play.csv", "r") as f:
#     element=f.read().replace("'", "").split(", ") 
# f.close()
        
f.close()