#error_pass.py

try:
    # 설정파일을 읽으려는 시도
    with open("설정파일.txt", 'r') as f:
        config = f.read()
except FileNotFoundError:
    pass # 설정파일이 없어도 계속 진행

# 프로그램의 주요기능은 계속 수행
print("프로그램이 정상적으로 실행됩니다.")
