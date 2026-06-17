# calculator.py

result = 0

def add(num):
    global result
    result += num # 결과값(result)에 입력값(num) 더하기
    return result # 결과값 반환
print(add(3))
print(add(4))
