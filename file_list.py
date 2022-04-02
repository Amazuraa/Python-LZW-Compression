from os import listdir, remove
from os.path import isfile, join, getsize
import math

def get_file_list():
    # -- get file name from directory
    fileList = [f for f in listdir("./compressed/") if isfile(join("./compressed/", f))]

    # -- get size
    for i in range(len(fileList)):
        size = getsize("./compressed/" + fileList[i])

        # -- count size
        size_name = ("B", "KB", "MB", "GB")
        j = int(math.floor(math.log(size, 1024)))
        p = math.pow(1024, j)
        s = round(size / p, 2)

        # -- append to list
        fileList[i] = (fileList[i], "%s %s" % (s, size_name[j]))

    return fileList

def remove_file(name):
    remove("./compressed/" + name)
    return "Success"