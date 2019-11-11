import requests, zipfile, io, shutil, os

VERBOSE = True
DESTINATION = "./files"
os.mkdir(DESTINATION)

LEN = 163536

data = open("files.txt", "r")

i = 0
for line in data:
    i += 1

    words = line.split(" ")
    url = words[-1].strip()

    req = requests.get(url, stream=True)
    z = zipfile.ZipFile(io.BytesIO(req.content))
    z.extractall()

    filename = url.split("v2/")
    filename = filename[-1].strip()
    filename = filename[0:-4] #remove .zip

    if VERBOSE and (i%10 == 0):
        print( str(i) + " / " + str(LEN) )

    shutil.move("./" + filename, DESTINATION)
