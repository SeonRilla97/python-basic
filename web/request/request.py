from fastapi import APIRouter, Request

'''
Request 객체

1. Body를 Json으로 파싱 가능
    await request.json()
2. Form Data를 파싱 
    await request.form()
'''

router = APIRouter()


@router.get("/items")
async def req_read_item(request: Request):
    client_host = request.client.host
    headers = request.headers
    query_params = request.query_params
    url = request.url
    path_params = request.path_params
    method = request.method


    return {
        "client_host": client_host, 
        "headers": headers, 
        "query_params": query_params, 
        "url": url, 
        "path_params": path_params, 
        "method": method, 
    }