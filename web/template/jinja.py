from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi import Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="./static/templates")

class Item(BaseModel):
    name: str
    price: int
    is_sale: bool = False

@router.get("/items/{id}", response_class=HTMLResponse)
async def template_item(request: Request, id: str, q: str | None = None):
    '''
    template engine 사용 시 반드시 request 선언 필수
    '''

    # 내부적으로 여러 아이템(리스트) 생성
    items = [
        Item(name="사과", price=1000, is_sale=True).model_dump(),
        Item(name="바나나", price=2500, is_sale=False).model_dump(),
        Item(name="체리", price=3000, is_sale=True).model_dump()
    ]

    return templates.TemplateResponse(
        request=request,
        name="item.html",
        context={"id": id, "items": items, "q": q}
    )