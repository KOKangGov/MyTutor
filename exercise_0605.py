treeHit = 0
while treeHit < 10:
    treeHit = treeHit + 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무가 넘어갑니다.")

prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while number != 4:
    print(prompt)
    number = int(input())
    
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 드립니다.")
    coffee = coffee -1
    print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

# coffe.py
coffee = 10
while True:
    money = int(input("돈을 넣어주세요: "))
    if money == 300:
        print("커피를 한잔 드립니다.")
        coffee = coffee - 1
    elif money > 300:
        print(f"거스름돈 {money -300}를 드립니다.")
        coffee = coffee - 1
    else:
        print("돈을 돌려드립니다. 커피는 드리지 않습니다.")
    print(f"남은 커피의 양은 {coffee}개 입니다.")
    if coffee == 0:
        print("커피가 모두 팔렸습니다. 판매를 중지합니다.")
        break

a = 0
while a < 10:
    a = a + 1
    if a % 2 == 0: continue
    print(a)
    
while True:
    print("Ctrl+C를 눌러야 while문을 빠져나갈 수 있습니다.")

count = 0
while count < 4:
    print(f"카운트: {count}")
    count += 1
else:
    print("while문이 종료되었다.")

count = 0
while count < 5:
    if count == 5:
        break
    print(f"카운트: {count}")
    count += 1
else:
    print("while문이 정상 종료되었습니다.")

i = 2
while i <= 3:
    j = 1
    while j <= 9:
        print(f"{i} x {j} = {i*j}")
        j += 1
    i += 1