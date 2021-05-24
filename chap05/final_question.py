# 1번
def f(x):
    return x*2 + 1

print(f(10))

def f(x):
    return x*x + 2*x + 1

print(f(10))

# 2번

def mul(*values):
    output=1
    for i in values:
        output = output * i

    return output

print(mul(5, 7, 9, 10))

# 3번
