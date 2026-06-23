# euc_kr.py

# WSL환경에 터미널 출력 인코딩을 강제로 맞춰주기
import sys
import io

sys.stdout =io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# 1. euc-kr로 작성된 파일 읽기
with open('euc-kr.txt', encoding='euc-kr') as f:
    data = f.read()  # 유니코드 문자열
    print(data)

# 2. unicode 문자열로 프로그램 수행하기
data = data + "\n" + "추가 문자열"

# 3. euc-kr로 수정된 문자열 저장하기
with open('euc-kr.txt', encoding = 'euc-kr', mode = 'w') as f:
    f.write(data)