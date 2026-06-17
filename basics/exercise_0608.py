# %%
test_list = ['one', 'two', 'three']
for i in test_list:
    print(i)
# %%
a = [(1, 2), (3, 4), (5, 6)]
for (first, last) in a:
    print(first + last)

# %%
# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점 이상이면 합격이고 그렇지 않으면 불합격이다. 합격인지, 불합격인지 결과를 보여 주시오.

marks = [90, 25, 67, 45, 80]
number = 0
for mark in marks:
    number = number + 1
    if mark >= 60:
        print(f"{number}번 학생은 합격입니다.")
    else:
        print(f"{number}번 학생은 불합격입니다.")
        
# %%
marks = [90, 25, 67, 45, 80]

number = 0
for mark in marks:
    number = number + 1
    if mark < 60:
        continue
    print(f"{number}번 학생 축하합니다. 합격입니다.")

# %%
a = range(10)
a
# %%
a = range(1, 11)
a
# %%
add = 0
for i in range(1, 11):
    add = add + i

print(add)

# %%
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60:
        continue
    print(f"{number+1}번 학생 축하합니다. 합격입니다.")

# %%

for i in range(2, 10):
    for j in range(1, 10):
        print(i*j, end = " ")
    print('')

# %%

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num*3)

print(result)

# %%

a = [1, 2, 3, 4]
result = [num * 3 for num in a]

print(result)


# %%

a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]  # 표현식 for 항목 in 반복가능객체 if 조건문

print(result)

# %%

result = [x*y for x in range(2, 10)
              for y in range(1, 10)]
print(result)


# %%

for i in range(10):
    if i == 5:
        break
    print(i)

# %%

for i in range(5):
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# %%

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("for 문이 정상 종료되었습니다.")

# %%

fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# %%

fruits = ['apple', 'banana', 'orange']
for i, fruit in enumerate(fruits, start =1):
    print(f"{i}등: {fruit}")

# %%

names = ['홍길동', '김철수', '이영희']
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name}씨: {score}점")

# %%

names = ['홍길동', '김철수', '이영희']
scores = [85, 90, 78]
for name, score in zip(names, scores):
    print(f"{name}씨: {score}점")
    if score <= 80:
        print(f"{name}씨 불합격입니다.")

# %%
