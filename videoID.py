import re
# idlength=11
count=int(input("Enter the number of Songs: "))

with open("id.csv", "a") as f:
    for i in range(count):
        url = input("Enter the URL: ")
        video_id = re.findall(r"watch\?v=(\S{11})", url)[0]

        # copy the video id to clipboard
        # import pyperclip
        # pyperclip.copy(video_id)

        #write the video id to a id.csv in append mode
        f.write(", '"+video_id+"'")
        
        i+=1

f.close()

