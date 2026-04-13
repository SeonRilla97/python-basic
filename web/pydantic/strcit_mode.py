from pydantic import BaseModel, ValidationError, ConfigDict, Field
from typing import List, Annotated  
from fastapi.exceptions import RequestValidationError


'''
기본적으로 Pydantic은 묵시적 타입 변환을 지원한다.
    age : int = "29" -> 29

필요시 엄격한 타입 검증을 위해 strict mode를 사용한다.

Strict Mode 

1. 모델 전체에 적용
    model_config = ConfigDict(strict=True)

2. 특정 필드에 적용
    id : Annotated[int, Field(strict=True)]
    age : int = Field(default=None, strict=True)

유효성 검사 실패 시 다음의 에러가 발생된다. <- 이왕 쓸거면 ValidationError로 통일하자. 
    ValidationError <- RequestValidationError :  ValidationError를 감싼 Exception

어차피 DTO <-> Service Layer에서 변환할꺼니 strict mode는 사용하지 않는다. (??)
'''

class Address(BaseModel):
    street: str
    city: str
    country: str

class User(BaseModel):
    # model_config = ConfigDict(strict=True) # 모델 전체에 타입 엄격하게 검증

    id : Annotated[int, Field(strict=True)] # 해당 필드만 엄격하게 검증
    name: str
    # age: int | None = None
    age : int = Field(default=None, strict=True) # 해당 필드만 엄격하게 검증
    email: str
    address: List[Address]



try:
    user = User(
        id=1, # 문자열 abc로 바꾸면 ValidationError로 잡힌다. 
        name="홍길동",
        age="29", # 문자열 값을 자동 파싱한다. (strcit Mode가 아닐 시)
        email="test@test.com",
        address=[{"street": "강남대로", "city": "서울시", "country": "대한민국"}]
    )
except ValidationError as e:
    print("validation error happened")
    print(e)