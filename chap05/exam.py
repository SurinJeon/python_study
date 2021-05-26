from builtins import print

# 1번
def dan(num):
    for i in range(1, 10):
        print("{0} * {1} = {2:2}".format(num, i, num * i))


def gugudan():
    for i in range(2, 10):
        dan(i)


def gugudan2():
    for j in range(1, 10):
        for i in range(2, 10):
            print("{} * {} = {:2}  ".format(i, j, i*j), end="  ")
        print()


if __name__ == "__main__":
    gugudan2()


# 2번

def solution(array, commands):
    answer = []
    temp = []
    for c in commands: # [2, 5, 3]
        for i in range(c[0] - 1, c[1]):
            temp.append(array[i])

        temp.sort()
        answer.append(temp[c[2]-1])
        temp.clear()

    return answer

print()


if __name__ == "__main__":
    array = [1, 5, 2, 6, 3, 7, 4]
    commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]

    result = solution(array, commands)

    print(type(result)) # list
    print(result) # [5, 6, 3]

# 2-1 list comprehension

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
temp = []
answer2 = [sorted(array[a - 1:b])[c -1] for a, b, c in commands]


print(answer2)

print()


# 3번
list_a = [[10, 20], [30, 40, 70, 110], [50, 60], [80, 90, 100]]
dict_a = {'k': {'a': 10, 'b': 20}, 'l': {'a': 10, 'b': 20, 'c': 40}, 'm': {'a': 10}}

for a in range(len(list_a)):
    for b in list_a[a]:
        print(b, end="  ")
    print()

print()

for key in dict_a:
    print(key, "=>", end=" ")
    for k in dict_a[key]:
        print("{} : {}".format(k, dict_a[key][k]), end=" ")
    print()

