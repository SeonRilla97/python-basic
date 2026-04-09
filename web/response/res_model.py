
from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi import status, Form
from pydantic import BaseModel

router = APIRouter()

class Item(BaseModel):
    name: str
    description: str
    price: float 
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "매운 새우깡",
                    "description": "아주 매운 과자입니다.",
                    "price": 2000.0,
                    "tax": 200.0
                }
            ]
        }
    }

class ItemResp(BaseModel):
    # 다음의 속성은 반드시 있어야함 (강제성 부여)
    name: str
    description: str
    price_with_tax: float 
    
@router.post("/create_item", response_model=ItemResp, status_code=status.HTTP_201_CREATED)
def create_item_rmodel(item: Item):
    '''
    [Response Model]
        - 응답으로 반환할 데이터의 구조를 정의
        - response_model 인자에 Pydantic 모델을 전달
        - 응답 데이터가 Pydantic 모델과 다를 경우 자동으로 변환

        - status_code 인자에 응답 상태 코드를 전달 (Return에서 전달할 수 없으니, annotation으로 전달)
    '''
    if item.tax is None:
        price_with_tax = item.price
    else:
        price_with_tax = item.price +  item.tax

    return ItemResp(
        name=item.name,
        description=item.description,
        price_with_tax=price_with_tax
    )
