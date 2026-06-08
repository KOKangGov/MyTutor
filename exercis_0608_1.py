# 이제 함수 공부임
def add(a, b):  # 함수 이름은 add이고, 2개의 값을 받는다
    return a + b  # 반환(출력)값은 2개 입력값을 더한 값이다.

#%%

a =3
b = 4
c = add(a, b)
print(c)

# %%

def add(a, b): # a, b는 매개변수(parameter)
    return a + b
print(add(3, 4)) # 3, 4는 인수(arguments)

# %%

def sub(a, b):
    return a - b
result = sub(a = 7, b = 3)
print(result)

result = sub(a=5, b=3)
print(result)

# %%

def add_many(*args):
    result = 0
    for i in args:
        result = result + i # *args는 입력받은 모든 값을 더한다.
    return result

# %%

result = add_many(1, 2, 3)
print(result)

# %%

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

# %%

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1,2,3,4,5)
print(result)

result = add_mul('mul', 1,2,3,4,5)
print(result)

# %%
# 키워드 매개변수, kwargs

def print_kwargs(**kwargs):
    print(kwargs)

# %%

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

print_kwargs(name = '홍길동', age=24, city='서울', job='개발자')

# %%

def create_profile(**info):
    print("==프로필 정보==")
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(이름='김철수', 나이='30', 직업='프로그래머', 취미='독서')

# %%

def mixed_function(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"추가 인수들: {args}")
    print(f"키워드 인수들: {kwargs}")

mixed_function('홍길동', 1, 2, 3, age=25, city='서울')

# %%

def say_myself(name, age, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살 입니다.")
    if man:
        print("남자 입니다.")
    else:
        print("여자 입니다.")

# %%
say_myself("강경오", 34)
# %%

say_myself("강경오", 34, True)

# %%

say_myself("강경오", 35, False)

# %%
