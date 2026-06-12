# filter1.py

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))


# lambda함수를 이용하면 더 쉽게 만들수 있음
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))