from pydantic import BaseModel, Field, ValidationError, EmailStr
from typing import Annotated

# ====================================================================================
# [Pydantic V2 공식 문서 기반 프로젝트 공통 표준]
# 1. 제약조건(Metadata): 무조건 Annotated 내부에 Field(...)로 정의한다.
# 2. 기본값(Default): 무조건 우측 = 연산자로 할당한다 (정적 타입 체커 지원 목적).
# 3. Optional(선택값): 파이썬 3.10+ 문법인 `T | None` 을 사용하며, 반드시 `= None` 을 할당해야 Pydantic V2에서 선택값으로 동작한다.
# ====================================================================================

'''
입력 데이터는 다음의 방식으로 나뉜다.

    1. 필수값 + 제약조건 없음
    2. 필수값 + 제약조건 있음
    3. 선택값 + 제약조건 없음
    4. 선택값 + 제약조건 있음
    5. 필수 타입이지만 기본값이 존재하는 경우

제약 조건의 종류 (기초 제약조건에 대해 Docs 확인 필요)
    기본적으로 *Type 을 통해 많이 사용하는 제약조건을 제공한다.
        기본 타입 : https://pydantic.dev/docs/validation/latest/api/pydantic/standard_library_types/
        기본 데이터 : https://pydantic.dev/docs/validation/latest/api/pydantic/types/
        네트워크 관련 : https://pydantic.dev/docs/validation/latest/api/pydantic/networks/
        추가 타입 : https://pydantic.dev/docs/validation/latest/api/pydantic-extra-types/pydantic_extra_types_country/
'''
class User(BaseModel):
    # [Case 1] 필수값 + 제약조건 없음
    name: str

    # [Case 2] 필수값 + 제약조건 있음
    # -> Annotated 패턴 사용
    email: EmailStr # 문자열 Email 검증
    age: Annotated[int, Field(gt=0, lt=100, description="나이")]

    # [Case 3] 선택값 + 제약조건 없음
    # -> V2부터는 `| None`만 쓴다고 선택값이 되지 않습니다. 반드시 `= None`이 필요합니다!
    nickname: str | None = None

    # [Case 4] 선택값 + 제약조건 있음
    # -> 제약조건은 Annotated에 넣고, 기본값은 우측에 뺍니다. (가장 완벽한 공통화 통일 방식)
    description: Annotated[str | None, Field(max_length=50, description="자기소개")] = None

    # [Case 5] 기본값이 존재하는 필수 타입 필드 (선택값과 동일한 원리)
    is_active: Annotated[bool, Field(description="활성 여부")] = True

try: 
    user = User(name="홍길동", email="test@test.com", age=20)
    print(user)
except ValidationError as e:
    print(e) 