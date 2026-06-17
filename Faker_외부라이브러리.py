# Faker_외부라이브러리

from faker import Faker
fake = Faker()
fake.name() # 영문이름 무작위 생성

fake = Faker('ko-KR')
fake.name() # 한글이름 무작위 생성

fake.address() # 주소 무작위 생성

test_data = [(fake.name(),ㄷ fake.address()) for i in range(30)] # 30개의 무작위 데이터 생성

# fake.name() 이름
# fake.address() 주소
# fake.postcode() 우편번호
# fake.country() 국가명
# fake.company() 회사명
# fake.job() 직업명
# fake.phone_number() 전화번호
# fake.email() 이메일 주소
# fake.user_name() 사용자명
# fake.pyint(min_value=0, max_value=100) 0에서 100사이의 임의의 숫자
# fake.ip4_private()  IP주소
# fake.text() 임의의 문장 (한글 임의의 문장은 fake.catch_phrase() 사용)
# fake.color_name() 색상명
