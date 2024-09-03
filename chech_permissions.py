import json_read as json_read

def chech_permisson(path=""):
    if path == "":
        return False
    else:
        bool = json_read.read_permisson(path)
        return bool