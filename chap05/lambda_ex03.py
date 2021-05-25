#함수선언 (lambda)
power = lambda x: x * x
under_3 = lambda x: x < 3

#변수선언
list_input_a = [1, 2, 3, 4, 5]

#map() 함수 이용
output_a = map(power, list_input_a)
print("#map() 함수의 실행결과")
print("map(power, list_input_a): ", output_a)
print("map(power, list_input_a): ", list(output_a))
print()

#filter() 함수 이용
output_b = filter(under_3, list_input_a)
print("#filter() 함수의 실행결과")
print("filter(under_3, list_input_a)", output_b)
print("filter(under_3, list_input_a)", list(output_b))


#혹은 lambda식을 바로 넣기
output_c = map(lambda x: x * x, list_input_a)
print("#map() 함수의 실행결과")
print("map(lambda x: x * x, list_input_c): ", output_c)
print("map(lambda x: x * x, list_input_c): ", list(output_c))
print()

output_d = filter(lambda x: x < 3, list_input_a)
print("#filter() 함수의 실행결과")
print("filter(lambda x: x < 3, list_input_d)", output_d)
print("filter(lambda x: x < 3, list_input_d)", list(output_d))