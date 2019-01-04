from acrcloud.recognizer import ACRCloudRecognizer

config = {
    'host': 'eu-west-1.api.acrcloud.com',
    'access_key': '0a4de053f27f7532034cfa3164301c2a',
    'access_secret': 'UddPOzyu5uv8wgMYjwKBSannygJRkEVhtqaGuxOY',
    'debug': False,
    'timeout': 10
}

acrcloud = ACRCloudRecognizer(config)

print(acrcloud.recognize_by_file('/home/pranav/Desktop/myfinalProject/Test/csr.mp3', 0))

