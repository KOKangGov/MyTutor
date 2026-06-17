s1 = set([1, 2, 3])
s1

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
s1.union(s2)

a = True
b = False
type(a)

1 == 1
2 > 1
2 < 1

a = [1, 2, 3, 4, 5]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

x = 5
y = 10
x > 0 and y > 0

a = 1 # 변수는 이름표, 객체는 데이터(값)
b = "python"
c = [1, 2, 3]
id(a), id(b), id(c)

a = [1, 2, 3]
b = a
id(a), id(b)
a is b

a[1] = 4
a
b

from copy import copy
a = [1, 2, 3]
b = copy(a)
id(a), id(b)
a is b
b

a = [1, 2, 3]
b = a.copy()
b is a
b

a, b = ('python', 'life')
a

(a, b) = 'python', 'life'
a

[a, b] = ['python', 'life']
a

a = 3
b = 5
a, b = b, a
a
b

money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# indent_error.py
money = True
if money:
    print("택시를")
    print("타고")
        print("가라")
else:
    print("걸어가라")

x = 3
y = 2
x > y
x < y
x == y
x != y

money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 돈이 3000원 이상 있거나 카드가 있으면 택시를 타고 가고, 그렇지 않으면 걸어가라
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

1 in [1, 2, 3]
1 not in [1, 2, 3]

'a' in ('a', 'b', 'c')
'j' not in 'python'

# 만약 주머니에 돈이 있으면 택시를 타고 가고, 없으면 걸어가라
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 주머니에 돈이 있으면 가만히 있고, 주머니에 돈이 없으면 카드를 꺼내라
pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

# 주머니에 돈이 있으면 택시를 타고 가고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고 가고, 돈도 없고 카드도 없으면 걸어가라.
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    if card:
        print("택시를 타고 가라")
    else:
        print("걸어가라")
        
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

# 학점이 A이면 "탁월한 성적입니다."를, B이면 "우수한 성적입니다."를, C이면 "보통입니다."를, 그 외에는 "노력이 필요합니다."를 출력하라.
grade = 'B'
if grade == 'A':
    print("탁월한 성적입니다.")
elif grade == 'B':
    print("우수한 성적입니다.")
elif grade == 'C':
    print("보통입니다.")
else:
    print("노력이 필요합니다.")


grade = 'B'
match grade:
    case 'A':
        print("탁월한 성적입니다.")
    case 'B':
        print("우수한 성적입니다.")
    case 'C':
        print("보통입니다.")
    case _:
        print("노력이 필요합니다.")

grade = 'B'
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case _:
        print("불합격입니다.")

score = 85
if score >= 60:
    result = "합격"
else:
    result = "불합격"
print(result)

score = 85
result = "합격" if score >= 60 else "불합격"
print(result)

age = 19
status = "성인" if age >= 18 else "미성년자"
print(status)
