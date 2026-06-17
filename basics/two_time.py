# two_time.py

def two_times(numberList):
    result =[]
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)

# map함수를 이용하여 
def two_times(x):
    return x*2

list(map(two_times, [1, 2, 3, 4]))

# lambda 함수를 사용하면
list(map(lambda a: a*2, [1, 2, 3, 4]))
