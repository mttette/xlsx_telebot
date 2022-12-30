import json


#TODO 
# save data function
# load data function
# data not var pls

text_messages = {
    "welcome" : "",
    "error":"",
}

def set(obj,path="data.json"):
    with open(path,"w") as file:
        json.dump(obj,file,indent=2)
    return 

def get(path="data.json"):
    obj = None
    with open(path,"r") as file:
        obj = json.load(file)
    
    return obj
