# generator2.py

import time

def longtime_job():
    print("job start")
    time.sleep(1)  # 1초 지연 - 실제로는 데이터베이스 조회, 파일처리 등 시뮬레이션
    return "Done"

# 리스트 컴프리헨션: 5번의 작업을 모두 실행하여 리스트로 만든다.
# list_job = [longtime_job() for i in range(5)]
# print(list_job[0])  # 첫번째 결과만 필요한 상황

# 제너레이터 표현식: 함수를 미리 실행하지않고 필요할 때만 실행
gen_job = (longtime_job() for i in range(5))
print(next(gen_job)) # 첫번째 값만 요청