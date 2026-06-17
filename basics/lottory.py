# lottory.py

import random

def random_lot(data):
    number = random.choice(data)
    data.remove(number)
    return number

if __name__ == "__main__":
    data = list(range(1, 46))
    for _ in range(6):
        print(random_lot(data))

# sample함수 이용
import random
if __name__=="__main__":
    data = list(range(1, 46)) # 1~45 사이의 숫자 중에서
    lotto_numbers = random.sample(data, 6) # 6개의 숫자만 무작위로 뽑아라
    print(lotto_numbers)

