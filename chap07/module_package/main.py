# import test_package.module_a as a
# import test_package.module_b as b
# init을 만들어서 모두 불러오기 하면 됨
from test_package import *

print(module_a.variable_a)
print(module_b.variable_b)