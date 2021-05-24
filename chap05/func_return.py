# return only
def return_test():
    print("A 위치입니다.")
    return
    print("b 위치입니다.")

return_test()

# return with data
def return_test():
    return 100

value = return_test()
print(value)

# return none
def return_test2():
    return

value2 = return_test2()
print(value2)
