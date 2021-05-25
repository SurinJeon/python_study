with open("info.txt", "r") as file:
    for line in file:
        # 변수선언
        (name, weight, height) = line.strip().split(", ")

        # 데이터 문제 있는지 확인과정
        if(not name) or (not weight) or (not height):
            continue

        # 결과 계산하기
        bmi = int(weight) / ((int(height) / 100) **2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상체중"
        else:
            result = "저체중"

        #출력하기
        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))

        print()
