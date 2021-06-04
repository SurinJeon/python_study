# 2번
output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
#list_bin = {}
#for j in output:
#    if "{:b}".format(j).count("0") == 1:
#        list_bin[j] = "{:b}".format(j)

print(sum(output))

# 시험 1번
# 구구단을 출력하는 함수( dan(num) )를 작성하고 dan(4) 결과를 아래와 같이 출력하시오.
def dan(num):
    print("==== {}단 ====".format(num))
    for i in range(1, 10):
        print("{} * {} = {}".format(num, i, num*i))

dan(4)


# 시험 2번
def gu_gu_dan(start, end):
    for j in range(start, end + 1):
        dan(j)


gu_gu_dan(2, 4)

#시험 5번
list_a = []

for i in range(11):
    list_a.append(i)

print("list_a = ", list_a)

list_even = [e for e in list_a if e % 2 == 0]
list_odd = [o for o in list_a if o % 2 == 1]

print("list_even = ", list_even)
print("list_odd = ", list_odd)
