# 2번
output = [i for i in range(1, 101) if "{:b}".format(i).count("0") == 1]
#list_bin = {}
#for j in output:
#    if "{:b}".format(j).count("0") == 1:
#        list_bin[j] = "{:b}".format(j)

print(sum(output))

# 합계