1+1
print(1+1)
#%%
1+1

# %%
1+1
# %%
1+1
# %%
1+2
# %%
3/2.4
# %%
3*9
# %%
a=1
b=2
c=3
a+b+c
# %%
a="python"
print(a)
# %%
a=python
a
# %%
a="python"
a
# %%
a=3
if a > 1:
    print("a는 1보다 큽니다.")
# %%
for a in [1, 2, 3]:
    print(a)
# %%
i=0
while i < 3:
    i = i + 1
    print(i)
# %%
def add(a, b):
    return a + b
add(3, 4)
# %%
# hello, py
print("Hello World")
# %%
# editor.py
a = "python"
print(a)
print(1 + 1)
# %%
print("'어떤 프로그래밍 언어이든 그 언어의 자료형을 알고 이해할 수 있다면 이미 그 언어의 절반을 터득한 것이나 다름없다'라는 말이 있다. 자료형이란 프로그래밍을 할 때 쓰이는 숫자, 문자열 등과 같이 자료 형태로 사용하는 모든 것을 뜻한다.")
# %%a
# 정수형
a = 123
a = -178
a = 0
# 실수형
a = 1.2
a = -3.45
a = 4.24E10
a = 4.24e-10
# 8진수(octal) 0o로 시작
a = 0o177
print(a)
#16진수(hexadecimal) 0x로 시작
a = 0x8ff
b = 0xABC
print(b)

# %%
a = 3
b = 4
a + b
a * b
a / b
# %%
a = 3
b = 4
a ** b
# %%
7 % 3
3 % 7
# %%
7 / 4
7 // 4
# %%
a = 1
a = a + 1
print(a)

a = 1
a += 1
print(a)

a = 2
a *= 3
print(a)
# %%
"Life is too short, You need Python"
"a"
"123"

food = "Python's favorite food is perl"
food

food = 'Python's favorite food is perl'
food

say = '"Python is very easy." he says'

food = 'Python\'s favorite food is perl'
say = "\"Python is very easy.\"he says."

multiline='''
Life is too short
You need python
'''
print(multiline)

multiline="""
Life is too short
You need python
"""
print(multiline)

head = "Python"
tail = " is fun!"
head + tail

a = "Python"
a * 2

# multistring.py
print("=" * 50)
print("My Program")
print("=" * 50)

a = "Life is too short"
len(a)

a = "Life is too short, You need Python"
a[3]
b = a[0] + a[1] + a[2] + a[3]
b
a[0:4]
a[0:5]
a[12:17]

a = "20260522rainy"
date = a[:8]
weather = a[8:]
date
weather

a = "Pithon"
a[:1]
a[2:]
a[:1] + 'y' + a[2:]

"I eat %d apples." % 3
"I eat %s apples." % "five"

number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)
s