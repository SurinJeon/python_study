def print_hello():
    print("안녕하세요")


def call_10_time(func): #함수를 매개변수로 전달할 수 있음
    for i in range(10):
        func()


call_10_time(print_hello)