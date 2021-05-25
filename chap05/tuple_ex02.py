from pip._internal.utils.misc import enum

tuple_test1 = (10) # << 이건 tuple이 아니고 그냥 int로 인식함...

tuple_test2 = (10, ) # << tuple 됨(,를 붙여야된다)
list_test1 = [1]


print("tuple_test1", tuple_test1, type(tuple_test1), end='\n\n')
print("tuple_test2", tuple_test2, type(tuple_test2), end='\n\n') # tuple 맞음
print("list_test1", list_test1, type(list_test1), end='\n\n')

[a, b] = [10, 20]
(c, d) = (10, 20)
print("a:", a, ",","b:", b, end="\n\n")
print("c:", c, ",","d:", d, end="\n\n")

