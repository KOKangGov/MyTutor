# exercise_0609_2

for i in range(1, 11):
    data = f"{i}번째 줄입니다."
    print(data)
    

while True:
    data = input()
    if not data: break
    print(data)

with open("test.txt", "w") as f:
    content = "Hello, Python!"
    f.write(content)
print(content)

with open("한글파일.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)