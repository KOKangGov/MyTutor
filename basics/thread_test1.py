# thread_test1.py

import time
import threading # 스레드를 생성하기 위해서는 threading모듈이 필요하다.

def long_task():
    for i in range(5):
        time.sleep(1)
        print(f"Working: {i}\n")

print("Start!!")

threads = []
for i in range(5):
    t = threading.Thread(target=long_task) #스레드를 생성한다.
    threads.append(t)

for t in threads:
    t.start() # 스레드를 생성한다.

for t in threads:
    t.join() # join으로 스레드가 종료될때까지 기다린다.

print("End!!")