import datetime

print("#현재 시간 출력하기")

now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("#시간을 포맷에 맞춰서 출력하기")
output_a = now.strftime("%Y.%m.%d. %H:%M:%S")