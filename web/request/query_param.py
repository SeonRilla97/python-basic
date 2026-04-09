from fastapi import APIRouter

router = APIRouter()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@router.get("/items/")
async def read_items_with_various_queries(
    skip: int, 
    limit: int = 2, 
    keyword: str | None = None
):
    '''
    요청 파라미터(Query Parameter) 선언 방식

    URL 경로에 없는 함수의 매개변수들은 모두 Query Parameter로 인식되며,
    항상 Pydantic과 연관되어 자동으로 형변환 및 검증이 이루어집니다.

    [필수 인자]
    - **skip** (`int`) : 
      - 타입 힌트(`int`)를 통해 강제성이 부여되며, 요청 시 반드시 쿼리에 포함해야 에러가 나지 않습니다.

    [선택 인자]
    - **limit** (`int = 2`) : 기본값이 있는 선택 인자
      - 쿼리로 값을 넘기지 않으면 자동으로 Default 값(2)이 입력됩니다.

    - **keyword** (`str | None = None`) : 선택 인자 (None 허용)
      - 파이썬 3.10 이상의 최신 문법으로, 값이 없을 수도 있음을 명시합니다.

    ---
    [사용하지 않는 방식 요약]
    - `Optional[Type]` (기본값 없음) : 명칭은 Optional이나 통신상 필수로 강제되어 개발자 혼란을 유발하므로 안티패턴. ❌
    - `Optional[Type] = None` : `Type | None = None` 과 기능은 완벽히 동일하나, 코드가 길어지고 구형 문법이라 비추천. ❌
    '''
    
    # 1. skip과 limit을 활용하여 데이터 자르기 (페이징)
    if limit is None:
        result_items = fake_items_db[skip:]
    else:
        result_items = fake_items_db[skip : skip + limit]
    
    # 2. 결과물 조립
    response = {
        "items": result_items,
        "message": "권장 방식 쿼리 파라미터 적용 성공!"
    }
    
    # 3. 추가 선택 파라미터(keyword)가 채워져 들어왔다면 응답에 추가
    if keyword:
        response["keyword"] = keyword
        
    return response