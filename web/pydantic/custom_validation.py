from pydantic import BaseModel, field_validator, model_validator

'''
커스텀 유효성 검사
    field_validator : 단일 필드 검증
    model_validator : 여러 필드 검증

    1. 서비스에서 필요한 제약조건 구현
    2. 여러 필드를 이용해 제약조건 구현
'''

class User(BaseModel):
    username: str
    password: str
    confirm_password: str

    @field_validator("username")
    def validate_name(cls, v: str) -> str: # cls : 클래스 메소드임을 선언 / self : Object 메소드임을 선언
        if not v.strip():
            raise ValueError("Name must contain only alphabetic characters") # Python 내장 에러
        return v

    @field_validator("password")
    def validate_password(cls, v: str) -> str:
        if len(v) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if not any(chart.isdigit() for chart in v): # 숫자가 하나라도 없으면 에러
            raise ValueError("Password must contain at least one digit")
        if not any(char.isalpha() for char in v): # 문자가 하나라도 없으면 에러
            raise ValueError("Password must contain at least one alphabetic character")
        return v

    @model_validator(mode="after") # 개별 필드 검증 후 가장 마지막 검증
    def validate_password(cls, values):
        password = values.password
        confirm_password = values.confirm_password
        if password != confirm_password:
            raise ValueError("Passwords do not match")
        return values