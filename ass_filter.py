import json
import os

# load config
with open("config.json", "r") as file:
    config = json.load(file)
    directory = config["directory"]
    keywords = config["keywords"]
    print("load config...")
    print("directory:", directory)
    print("keywords:", keywords)

# get file list
assfiles = []
print("\nFound the following ass files in directory:")
for filename in os.listdir(directory):
    if filename.endswith(".ass"):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            print(filepath)
            assfiles.append(filepath)

# output ass
for assfile in assfiles:
    with open(assfile, "r") as file:
        content = file.readlines()
    ever_matched = False
    output = ""
    for line in content:
        if line.startswith("Dialogue"):
            comment = line.split("}")[-1].split('\n')[0]
            match = False
            for keyword in keywords:
                if keyword == comment:
                    match = True
                    ever_matched = True
                    break
            if match:
                continue
        output += line
    if ever_matched:
        with open(assfile, "w") as file:
            file.write(output)