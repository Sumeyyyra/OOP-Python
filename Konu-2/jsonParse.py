import json
#dosya çekerken load ,string vb. çekerken loads

with open("C:\\Users\\ustsu\\Desktop\\OOP-Python\\Konu-2\\jsondata.json") as jsonfile:
    users=json.load(jsonfile)
    for item in range(4):
        print(users[item]["name"])
        print(users[item]["address"]["city"])
    