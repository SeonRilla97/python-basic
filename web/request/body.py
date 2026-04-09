'''
Pydantic Model이 인자로 선언 시 Request Body로 인식한다.
'''
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    full_name: str | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "username": "john_doe",
                    "full_name": "John Doe"
                }
            ]
        }
    }

class Item(BaseModel): # Pydantic Model 사용 시 BaseModel을 상속받아야한다. 
    name: str # Required
    description: str | None = None # Optional
    price: float # Required
    tax: float | None = None # Optional
    
    # Swagger UI의 Example Value(기본 예제 값)를 지정해줄 수 있습니다.
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

@router.put("/items/{item_id}")
async def update_item(item_id: int, item: Item,user:User, q: str | None = None):
    '''
    Path / Query / Body 모두 사용한 예제

    [Body Parameter]
        - Pydantic Model을 인자로 선언 시 Request Body로 인식한다.
    '''
    # BaseModel을 dict으로 변환 : BaseModel은 수정이 불가능하기 때문에 dict으로 변환 후 사용한다.
    item_dict = {"item_id": item_id, **item.model_dump()}

    # Response에 추가할 데이터가 있다면 추가
    if q:
        item_dict.update({"q": q})

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})        

    # dict 반환 시 application/json으로 자동 변환
    return {"item": item_dict, "user": user}
