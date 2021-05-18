# 2번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print("- 100 이상의 수: ", number)

#3번
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수입니다.")
    else:
        print(number, "는 홀수입니다.")

for number in numbers:
    if number / 1 >= 100:
        print("{} 는 3 자릿수입니다.".format(number))
    elif number / 1 >= 10:
        print("{} 는 2 자릿수입니다.".format(number))
    else:
        print("{} 는 1 자릿수입니다.".format(number))

# 4번
list_of_list = [
    [1, 2, 3],
    [4, 5, 6, 7],
    [8, 9]
]

for list in list_of_list:
    for n in list:
        print(n, end="\n")

# 이중루프도 이런 식으로 가능함
list_result = [i for list in list_of_list for i in list]
print("list_result >> " , list_result)

# 5번
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in numbers:
    output[(number - 1) % 3].append(number)

print(output)

# 0~100까지 짝수만 list(even_list)에 저장하고 출력하시오.
# 0~100까지 홀수만 list(odd_list)에 저장하고 출력하시오.

even_list = []
odd_list = []

for number in range(101):
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

print(even_list)
print(odd_list)

# 혹은 list 미리 안 만들어 두고 list 안에 바로 반복문 돌리기
even_list2 = [i for i in range(101) if i % 2 == 0]
print(even_list2)