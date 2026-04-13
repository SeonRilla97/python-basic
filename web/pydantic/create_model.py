from pydantic import BaseModel
import json

# ==========================================
# 1. [기본 모델 및 포함(Nested) 모델 정의]
# ==========================================

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

# 필요 시 Python의 일반 클래스로 생성해서 비교해볼것 (Pydantic이 이를 변환해주는 역할을 한다.)
class User(BaseModel):
    name: str
    age: int
    email: str
    is_active: bool = True

# User를 상속받고, Address를 포함하는 확장 모델
class AdvancedUser(User):
    phone: str
    address: Address


# ==========================================
# 2. [객체 생성 방법 3가지]
# ==========================================

# 방법 1: Pydantic 일반 객체화 (생성 시 순서 상관없음, 필드명 선언 필수)
user_1 = AdvancedUser(
    name="홍길동", age=20, email="test@test.com", is_active=True, 
    phone="010-1234-5678", address=Address(street="강남대로", city="서울시", zip_code="12345")
)

# 방법 2: Dictionary Unpacking(**)을 통한 객체화
user_dict_data = {
    "name": "김철수", "age": 25, "email": "kim@test.com", "is_active": True, 
    "phone": "010-9876-5432", "address": {"street": "테헤란로", "city": "서울시", "zip_code": "54321"}
}
user_2 = AdvancedUser(**user_dict_data) # 또는 AdvancedUser.model_validate(user_dict_data)

# 방법 3: JSON 문자열 입력을 통한 객체화 (model_validate_json)
json_data = '{"name": "이영희", "age": 30, "email": "lee@test.com", "is_active": false, "phone": "010-1111-2222", "address": {"street": "부산대로", "city": "부산시", "zip_code": "98765"}}'
user_3 = AdvancedUser.model_validate_json(json_data)


# ==========================================
# 3. [Serialization(직렬화) / Deserialization(역직렬화)]
# ==========================================

'''
FastAPI는 요청/응답 시 내부적으로 자동 직/역직렬화를 수행합니다.
하지만 외부 통신(Redis, 외부 API 등) 시에는 아래처럼 "직접" 변환해야 합니다.

[수동 직/역직렬화 실무 로직 예시]
# 1. 직렬화 (객체 -> JSON 추출하여 외부 캐시 저장)
redis.set("user_123", target_user.model_dump_json())

# 2. 역직렬화 (외부에서 JSON 가져와서 -> 객체화)
user_obj = AdvancedUser.model_validate_json(redis.get("user_123"))
'''

target_user = user_1

# Pydantic Object -> Dict (직렬화)
dump_dict = target_user.model_dump()

# Pydantic Object -> JSON 문자열 (직렬화)
dump_json = target_user.model_dump_json()

# Dict -> Pydantic Object (역직렬화)
obj_from_dict = AdvancedUser.model_validate(dump_dict)

# JSON 문자열 -> Pydantic Object (역직렬화)
obj_from_json = AdvancedUser.model_validate_json(dump_json)