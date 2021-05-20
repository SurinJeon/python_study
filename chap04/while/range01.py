# p178
for i in range(5):
    print(str(i) + " = 반복변수")
print()

for i in range(5, 10):
    print(str(i) + " << 반복변수")
print()

for i in range(0, 10, 3):
    print(str(i) + " < 반복변수")
print()

# p179
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print("{}번째 반복: {}".format(i, array[i]))


for i in range(4, 0 - 1,  -1):
    print("현재 반복 변수: {}".format(i))
print()

# p180
for i in reversed(range(5)):
    print("현재 반복 변수: {}".format(i))