# program_1.py

result = gugu(2) # gugu함수에 2를 입력값을 주면 result 변수에 결과값 넣음

# result = [2,4,6,8,10,12,14,16,18] <-- 이런 결과값이 필요

# 실제로 프로그램을 짜면...

def gugu(n):
    result = []
    result.append(n*1)
    result.append(n*2)
    result.append(n*3)
    result.append(n*4)
    result.append(n*5)
    result.append(n*6)
    result.append(n*7)
    result.append(n*8)
    result.append(n*9)
    return result
print(gugu(2))

def gugu(n):
    result = []
    i = 1
    while i < 10:
        result.append(n * i)
        i = i+1
    return result
print(gugu(2))