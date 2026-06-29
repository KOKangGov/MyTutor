# 파이썬 3.5~3.8: typing 모듈 함수

from typing import List, Dict, Tuple, Optional

numbers: List[int] = [1, 2, 3]
user_info: Dict[str, int] = {"age": 30}


# 파이썬 3.9 이상: 내장 타입 사용 가능(권장)

numbers: list[int] = [1, 2, 3]
user_info: dict[str, int] = {"age": 30}


# typing 모듈이 여전히 필요한 경우

from typing import Optional, Union

#1. Optional -None이 가능한 경우
user_name: Optional[str] = None  # str 또는 None

#2. Union - 여러 타입이 가능한 경우
user_id: Union[int, str] = "jenny"  # 정수 또는 문자열


from typing import Callable, Any

# Collable - 함수 타입 지정
def process_data(callback: Callable[[int], str]) -> str:
    return callback(42)

# Any - 모든 타입 허용
unknown_data: Any = {"key": "value"}


# 파이썬 3.9 이상을 사용한다면

from typing import Optional, Union  # 필요한 것만 가져오기

# 기본 타입은 내장 타입 사용
scores: list[int] = [95, 87, 92]
user_data: dict[str, str] = {"name": "홍길동"}

# 특별한 경우에만 typing 모듈 사용
def find_user(user_id: int) -> Optional[dict[str, str]]:
    # 사용자를 찾으면 딕셔너리 반환, 없으면 None 반환
    if user_id > 0:
        return {"name": "홍길동", "email": "hong@example.com"}
    return None
