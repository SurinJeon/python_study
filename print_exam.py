print("#하나만 출력1")
print()

print("#하나만 출력2", "abcd", sep="\n", end="\n\n") #sep은 요소 사이에 \n(엔터 한번) 넣어라
print("결과", end="\n\n")

print(type('하나만'), type("하나만"), type(12), type(12.5), sep="\n", end="\n\n")

# print("안녕하세요" + 1)

print("안녕하세요"[0])
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])

print("안녕하세요"[0])
print()
print("안녕하세요"[0:4], end="\n\n")
print("안녕하세요"[:3], end="\n\n")
print("안녕하세요"[3:], end="\n\n")


hello = '안녕하슈'
print(type(hello), hello[:2], hello, sep="\n", end="\n\n")

# 입력받는 input함수
# res = input("입력하세요.")
# print("입력한 답은 ", res)

a = "10 11 a b 14".split(" ")
print(type(a), a, sep="\n")

x, y , z = 10, 20, 30
print(x, y, z, sep="\n") #파이썬은 이렇게 해도 10 20 30 알아서 나옴

print()

x, y = y, x #swap 이렇게 가능함
print(x, y, z, sep="\n")