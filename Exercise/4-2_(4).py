character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
        },
    "skill": ["횡베기", "세로베기", "차원참"]
    }
for key in character:
    if type(character[key]) is str:
        print(key, ":", character[key])
    elif type(character[key]) is int:
        print(key, ":", character[key])
    elif type(character[key]) is dict:
        for i in character[key]:
            print(i, ":", character[key][i])
    elif type(character[key]) is list:
        for i in character[key]:
            print(key, ":", i)
