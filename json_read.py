import json

def read_config(path=None):
    if path == None:
        return
    
    with open("json/config.json", "r") as read_file:
        file = json.load(read_file)

    result = file[path]
    return result

def read_permisson(path=None):
    if path == None:
        return
    
    with open("json/permissions_function.json", "+r") as read_file:
        file = json.load(read_file)

    result = file[path]
    return result    