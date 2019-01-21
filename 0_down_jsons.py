import os, time
import urllib.request, json

dirs = ["unprocessed_jsons", "processed_jsons", "images"]
for dir in dirs:
    if not os.path.exists(dir):
        os.makedirs(dir)

query_str = "test+whatever"
date_id="jan21" # unique id to differentiate
number_of_pages = 20
skip_from_i = 0

# 1.) download unprocessed json files by querying:
#    https://serpapi.com/search.json?q=Apple&tbm=isch&ijn=0


for i in range(skip_from_i,number_of_pages):
    print("Downloading", i, "/", number_of_pages)
    url_str = "https://serpapi.com/search.json?q="+query_str+"&tbm=isch&ijn="+str(i)
    with urllib.request.urlopen(url_str) as url:
        data = json.loads(url.read().decode())
        #print(data)

        twitterDataFile = open("unprocessed_jsons/"+date_id+"_images_"+str(i).zfill(3)+".json", "w")
        twitterDataFile.write(json.dumps(data, indent=4, sort_keys=True))
        twitterDataFile.close()

        time.sleep(2)

