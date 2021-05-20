# 2번
key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]
character = {}

for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)

# 3번
limit = 10000
i = 1
sum_value = 0

while True:
    sum_value = sum_value + i
    i += 1
    if sum_value > 10000:
        break


print("{}를 더할 때 {}을 넘으며 그 때의 값은 {}입니다.".format(i-1, limit, sum_value))
print()

# 4번
max_value = 0
a = 0
b = 0
list_max = [0]

for i in range(1, 100):
    j = 100 - i
    max_value = i * j
    list_max.append(max_value)

print(max(list_max))
