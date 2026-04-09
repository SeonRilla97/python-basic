from fastapi import APIRouter, Form
from typing import Annotated

router = APIRouter()

@router.post("/login")
async def login(username: str = Form(), 
                password: str = Form(), #필수
                country: Annotated[str, Form()] = None ):   # Optional 설정
    '''
    [Form]
    Form() 이없으면 Query로 인식한다.
    
    필수 값 : Form()
    선택 값 : Annotated[Type,Form()] = None
    '''
    return {"username": username, "password": password, "country": country}