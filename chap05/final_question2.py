# 1번
example = [[1, 2, 3], [4, [5, 6]], 7, [8, 9]]
result = []


def flatten(data):
    for d in data:
        if type(d) is int:
            result.append(d)
        elif type(d) is list:
            flatten(d)
    return result


print("원본: ", example)
print("변환: ", flatten(example))