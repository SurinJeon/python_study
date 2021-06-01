import os

print("현재 운영체제: ", os.name)
print("현재 폴더: ", os.getcwd())
print("현재 폴더 내부의 요소: ", os.listdir())


print(os.path.exists("hello"))

if not os.path.exists("hello"):
    os.mkdir("hello")

if os.path.exists("hello"):
    os.rmdir("hello")


with open("original.txt", "w") as file: #만들고(없으면 만들어짐)
    file.write("hello") #쓰고

os.rename("original.txt", "new.txt") #이름 바꾸기

os.remove("new.txt") #삭제하기 (unlink도 똑같은 것)


std_list = [1, "짱수린", 90, 80, 70], [2, "짱수린2", 92, 85, 72],

if not os.path.exists("std_list.txt"): #존재하지 않는다면
    with open("std_list.txt", "w", encoding="utf-8") as f:
        for std in std_list:
            format_str = "{}, {}, {}, {}, {}\n".format(std[0], std[1], std[2], std[3], std[4])
            f.write(format_str)


std_list2 = []
with open("std_list.txt", "r", encoding="utf-8") as f:
    for line in f: #한 줄씩 읽겠다는 뜻
        std = line.strip().split(", ")
        print("std: ", std, type(std))
        std = int(std[0]), std[1], int(std[2]), int(std[3]), int(std[4]) #숫자를 모두 int로 바꿔줌 
        std_list2.append(list(std)) #tuple로 들어가기 때문에 다시 list로 바꿔줌

print("std_list2 >> ", std_list2)

os.system("dir") #cmd에서 dir한 것과 같음

