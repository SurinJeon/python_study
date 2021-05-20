# 3번
numbers = [1, 2, 3, 4, 7, 5, 8, 4, 2, 8, 5, 8, 4, 1, 8, 5, 6, 9, 3]
counter = {}

for number in numbers:
    key = number
    if key in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)

# 4번
character = {
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기", "세게 베기", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str:
        print(key, " : ", character[key])
    elif type(character[key]) is int:
        print(key, " : ", character[key])
    elif type(character[key]) is dict:
       for i in character[key]:
            print(i, " : ", character[key][i])
    elif type(character[key]) is list:
        for j in character[key]:
            print(key, " : ", j)


















