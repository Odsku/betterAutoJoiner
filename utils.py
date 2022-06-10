import re, json

def strip(message):
    try:
        return json.loads(re.sub(r'\d+\{', '{', message))
    except:
        return json.loads(re.sub(r'\d+\[', '[', message))
