'''
서버의 기초적인 Swagger를 작성하는 방법에 대해서 정리

FastAPI는 기본적으로 /docs 경로로 Swagger가 생성된다.
'''
from fastapi import APIRouter

router = APIRouter()

@router.get("/swagger",
    summary="Swagger UI", # 1. Endpoint의 이름
    response_description="Swagger UI를 제공합니다.",
    tags=["swagger"] # 3. API의 그룹 (카테고리)
)
async def swagger():
    '''
    docstring 형식으로 Swagger Description 작성

    이것은 간단한 API입니다. 아래는 인자값 입니다.

    - **인자값 1** : 인자값 1에 대한 설명
    - **인자값 2** : 인자값 2에 대한 설명
    '''
    return {"message": "Swagger"}