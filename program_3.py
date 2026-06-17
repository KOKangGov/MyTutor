# program_3.py

#paging

def get_tatal_page(m, n):
    if m % n == 0:             # 나머지가 0인 경우
        return m // n          # 몫만 반환
    else:
        return m // n + 1      # 나머지가 0이 아닌 경우, 몫+1 을 반환

print(get_tatal_page(5, 10))
print(get_tatal_page(15, 10))
print(get_tatal_page(25, 10))
print(get_tatal_page(30, 10))