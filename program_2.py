# program_2.py

# 1000 미만의 자연수에서 3과 5의 배수 총합을 구하라

result = 0
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)
