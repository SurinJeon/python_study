list_a = ['a', 'b', 'c']

for e in list_a:
    print(e)


# enum을 사용해서 index와 같이 뽑아내기
for i, v in enumerate(list_a): #i와 v는 tuple임. list_a 안에 있는 것을 튜플로 담아서 뱉어줌
    print(i, v)


a, b = 97, 40
x, y = divmod(a, b) #a / b의 몫과 나머지를 tuple로 전달0
print("x=", x, "y=", y)