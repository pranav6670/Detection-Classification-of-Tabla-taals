from acrcloud.recognizer import ACRCloudRecognizer
import json

config = {
    'host': 'eu-west-1.api.acrcloud.com',
    'access_key': '0a4de053f27f7532034cfa3164301c2a',
    'access_secret': 'UddPOzyu5uv8wgMYjwKBSannygJRkEVhtqaGuxOY',
    'debug': False,
    'timeout': 10
}


acrcloud = ACRCloudRecognizer(config)

# Convert output 'str' from function to 'dict'
S = json.loads(acrcloud.recognize_by_file('/home/pranav/Desktop/myfinalProject/Test/csr.mp3', 0))

# Get required items from 'dict' and convert to 'list'
C = S['metadata']['music']

# Pop objects from list
A = C.pop()

# Get artist name from metadata
V = A['external_metadata']['deezer']
O = V['artists'].pop()

print("Artist name: ", O['name'])
print("Album name: ", A['album']['name'])
print("Release date: ", A['release_date'])
print("Title:", A['title'])
print("Label: ", A['label'])
print("Duration: ", A['duration_ms'], "ms")



