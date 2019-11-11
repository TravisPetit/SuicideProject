import requests, zipfile, io, shutil

DESTINATION = "./files"

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
    print(filename)

    #to = DESTINATION + filename
    #shutil.move("./" + filename, to)
    shutil.move("./" + filename, DESTINATION)
