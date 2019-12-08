import requests, zipfile, io, shutil, os
from datetime import datetime

VERBOSE = True
DESTINATION = "./files"
LEN = 89000

os.mkdir(DESTINATION)
data = open("files.txt", "r")

i = -1
for line in data:
    i += 1

    words = line.split(" ")
    url = words[-1].strip()

    filename = url.split("v2/")
    filename = filename[-1].strip()
    filename = filename[0:-4] #remove .zip

    try:
        req = requests.get(url, stream=True)

        z = zipfile.ZipFile(io.BytesIO(req.content))
        z.extractall()

        shutil.move("./" + filename, DESTINATION + "/" + str(i) + ".csv")

    except Exception as e:
        mssg = "Skipping file: {}, iteration: {}\n".format(filename, i)
        mssg += "--\n"
        mssg += "Exception instance: {}\nException arguments: {}\nException string: {}\n".format(type(e),e.args,e)
        mssg += "--"

        if VERBOSE: print(mssg)

        f = open("bad_indices.txt", "a+")
        f.write(str(i)+",")
        f.close()

    if VERBOSE and (i%10000 == 0):
        time = str(datetime.now().time().replace(microsecond=0))
        print(time + "   " + str(i) + " / " + str(LEN))

data.close()
