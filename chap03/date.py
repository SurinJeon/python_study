import datetime

# 현재 날짜
now = datetime.datetime.now()

# 출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print()

#혹은 format으로 쓰기
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# format numbering도 가능함
print("{0}년 {0}월 {1}일".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))

# 오전 오후 구분하기
if now.hour < 12:
    print("현재 시간은 {}시로 오전입니다.".format(now.hour))

if now.hour >= 12:
    print("현재 시간은 {}시로 오후입니다.".format(now.hour))

# 계절 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
