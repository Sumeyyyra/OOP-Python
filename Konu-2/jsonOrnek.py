import json

#json doyyası oluşturduk
data='{"ad":"volkan","soyad": "ak"}'

#datayı yükledik ve içine eriştik
j=json.loads(data)
print(j["ad"],j["soyad"])