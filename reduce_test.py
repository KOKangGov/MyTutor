# reduce_test.py

import functools

data = [1, 2, 3, 4, 5]
result = functools.reduce(lambda x, y: x+y, data)
print(result)

# functools.reduce함수로 최대값 구하기
num_list = [3, 2, 8, 1, 7, 9, 6]
max_num = functools.reduce(lambda x, y: x if x > y else y, num_list)
print(max_num)
