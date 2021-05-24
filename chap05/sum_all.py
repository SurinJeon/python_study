# sum all basic
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print("0 to 100 >> ", sum_all(0, 100))
print("0 to 1000 >> ", sum_all(0, 1000))
print("50 to 100 >> ", sum_all(50, 100))
print("500 to 1000 >> ", sum_all(500, 1000))


# summ all with default
def sum_all_default(start=0, end=100, step=1):
    output2 = 0
    for i in range(start, end + 1, step):
        output2 += i
    return output2

print("A", sum_all_default(0, 100, 10))
print("B", sum_all_default(end=100))
print("C", sum_all_default(end=100, step=2))