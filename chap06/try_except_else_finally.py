#try except 구문으로 예외 처리하기
try:
    number_input_a = int(input("정수 입력 > "))

    print("원의 반지름: ", number_input_a)
    print("원의 둘레: ", 2* 3.14 * number_input_a)
    print("원의 넓이: ", 3.14 * number_input_a * number_input_a)

except:
    print("정수를 입력해주세요.")
else:
    print("예외를 발생하지 않았습니다.")
finally:
    print("프로그램을 종료합니다.")