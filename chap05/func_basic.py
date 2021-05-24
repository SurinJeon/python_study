# basic
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()

# with parameter
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("hello world", 3)

