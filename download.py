import requests, zipfile, io, shutil, os

VERBOSE = True
DESTINATION = "./files"
os.mkdir(DESTINATION)

data = open("files.txt", "r")

for line in data:
    words = line.split(" ")
    url = words[-1].strip()

    req = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(req.content))
    z.extractall()

    filename = url.split("v2/")
    filename = filename[-1].strip()
    filename = filename[0:-4] #remove .zip

    if VERBOSE:
        print(filename)

    shutil.move("./" + filename, DESTINATION)
