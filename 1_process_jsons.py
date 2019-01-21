from os import listdir
from os.path import isfile, join
import json
from pprint import pprint
import urllib.request
import shutil

# 2.) process json files = down images in full res and then move json to a processed folder

folder = "unprocessed_jsons/"
move_jsons_path = "processed_jsons/"
save_folder = "images/"

json_paths = [f for f in listdir(folder) if isfile(join(folder, f))]
json_paths.sort()

for i in range(0,len(json_paths)):
    json_path = folder+json_paths[i]
    json_moved_path = move_jsons_path+json_paths[i]

    print("parsing JSON", i, json_path)

    with open(json_path) as f:
        data = json.load(f)

    #pprint(data)

    for image in data["images_results"]:
        filename = json_paths[i][0:-5] + "_" + ''.join(e for e in image["title"] if e.isalnum())
        link = image["original"]
        #print(filename)
        #print(image["original"])
        #print(image["thumbnail"])

        try:
            file = save_folder+filename+'.jpg'
            urllib.request.urlretrieve(link, file)

        except Exception as E:
            print(E, link)

    shutil.move(json_path, json_moved_path)

