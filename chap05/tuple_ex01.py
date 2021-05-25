tuple_test1 = (10, 20, 30)
#tuple_test2 = tuple(10, 20, 30) << 이거는 안됨...
tuple_test3 = 10, 20, 30
list_test1 = [10, 20, 30]

print("tuple_test1", tuple_test1, type(tuple_test1), end='\n\n')
print("tuple_test3", tuple_test3, type(tuple_test3), end='\n\n')
print("list_test1", list_test1, type(list_test1), end='\n\n')


# 변경해보기
list_test1[1] = 10
print("list_test1", list_test1, type(list_test1), end='\n\n')

# tuple_test1[1] = 100 << tuple은 이걸 지원하지 않음
# print("tuple_test1", tuple_test1, type(tuple_test1), end='\n\n') 