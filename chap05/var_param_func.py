# variable parameter
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)

        print()

print_n_times(3, "hi", "hello", "world")

# default parameter
def print_n_times_2(value, n=2):
    for i in range(n):
        print(value)

print_n_times_2("안녕하세요.")
