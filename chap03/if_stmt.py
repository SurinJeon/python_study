if True:
    print("True입니다.")
    print("정말 True입니다..!") #if문은 들여쓰기 한 것까지 인식함

if False:
    print("False")

print("aaa")

number = input("정수 입력 > ")
number = int(number)

if number > 0:
    print("양수입니다.")

if number < 0:
    print("음수입니다.")

if number == 0:
    print("0입니다.")