# decorate2.py

import time

def elapsed(original_func):
    def wrapper():
        start = time.time()
        result = original_func()
        end = time.time()
        print("함수 수행시간: %f 초" %(end - start))
        return result
    return wrapper

@elapsed
def myfunc():
    print("함수가 실행됩니다.")

# decorated_myfunc = elapsed(myfunc) # @elapsed 테코레이터로 인해 더 이상 필요하지않음
# decorated_myfunc()

myfunc()