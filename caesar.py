# caesar.py

# 시저암호: 알파벳을 일정한 수만큼 밀어서 다른 글자로 변환하는 것.

def caesar(word, key):
    result = ""
    for char in word:
        if char.isupper():                     # 대문자인 경우
            num = ord(char) - ord('A')         # 알파벳을 0~25 숫자로 변환
            shifted = (num + key) % 26         # key만큼 밀고, 26으로 나눈 나머지
            result += chr(shifted + ord('A'))  # 다시 알파벳으로 전환
        elif char.islower():                    # 소문자인 경우
            num = ord(char) - ord('a')
            shifted = (num + key) % 26
            result += chr(shifted + ord('a'))
        else:                                   # 공백, 특수문자인 경우
            result += char                      # 변환하지않고 그대로 유지
    return result

while True:
    word = input("문자열을 입력하세요(영어와 공백만 가능): ")  
    
    # 올바르지 않은 문자(알파벳 또는 공백도 아닌)가 있는지 검사
    has_invalid_char = False
    for char in word:
        if not char.isalpha() and not char.isspace():
            has_invalid_char = True
            break                               # 하나라도 잘못된 문자가 있으면 검사중단

    if has_invalid_char:
        print("X 오류: 숫자나 특수문자는 입력할 수 없습니다!\n")
    elif word.strip() == "":
        print("X 오류: 최소 한글자 이상의 영문자를 입력해 주세요\n")
    else:
        break                                # 올바른 입력이 들어오면 while 루프 탈출

key = int(input("적용할 숫자를 입력하세요: "))

print(f"암호화: {caesar(word, key)}")
