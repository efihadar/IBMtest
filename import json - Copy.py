import json
import requests
 
response = requests.get('https://google.com') 
 
# JSON data:
with open("/data/python/config.json", "r") as f:
     x = f.read()

# x = "{\"url\":\"https://google.com\"}"
 
# object to be appended
y = {"content":f"{response.text[:15]}"}
 
# parsing JSON string:
z = json.loads(x)
  
# appending the data
z.update(y)
 
# the result is a JSON string:
# print(json.dumps(z))

with open("/data/python/config.json", "w") as f:
    f.write(json.dumps(z))