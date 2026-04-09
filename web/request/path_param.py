from fastapi import APIRouter

router = APIRouter()


@router.get("/all")
async def req_read_item_all(): 
    '''
    [Path Parameter]

        - 고정 /item/all 등의 고정 경로는 Path Parameter보다 앞에 작성해야한다.
    '''
    return {"item_id": "all items"} # Dict 반환 시 application/json으로 변환

@router.get("/{item_id}")
async def req_read_item(item_id: int):
    '''
    [Path Parameter] : URL의 경로에 포함된 변수

        - 타입 힌트에 맞지 않은 데이터 들어올 시 pydantic이 에러를 반환한다.

    '''
    return {"item_id": item_id} # Dict 반환 시 application/json으로 변환

