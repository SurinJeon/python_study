dictionary = {
    "name":"7D 건조 망고",
    "type":"당절임"
}

# 요소 제거 전 출력
print("요소 제거 이전: ", dictionary)

# 제거
del dictionary["name"]
del dictionary["type"]

print("요소 제거 이후: ", dictionary)