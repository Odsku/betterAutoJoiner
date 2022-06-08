import os, json, re

def load_config(filename):
    configFile = open(filename)
    config = json.loads(configFile.read())
    configFile.close()
    return config

def strip(message):
    try:
        return json.loads(re.sub(r'\d+\{', '{', message))
    except:
        return json.loads(re.sub(r'\d+\[', '[', message))