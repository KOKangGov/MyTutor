# generator.py

def mygen():
    for i in range(1, 1000):
        result = i * i
        yield result
  # gen = (i * i for i in range(1, 1000)) <-- 이렇게 간략하게 표현 가능함
gen = mygen()

print(next(gen))
print(next(gen))
print(next(gen))