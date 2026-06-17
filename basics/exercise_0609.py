
# calculator
print("===간단한 계산기===")

#사용자로 부터 두 숫자 입력받기
num1 = float(input("첫번째 숫자를 입력하세요.: "))
num2 = float(input("두번째 숫자를 입력하세요.: "))

#계산결과 출력
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")
    