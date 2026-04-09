from fastapi import APIRouter
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
from fastapi import status, Form

router = APIRouter()


# JSON
@router.get("/json/{item_id}",response_class=JSONResponse)
def json_response(item_id: int):
    return JSONResponse(
        content={"item_id": item_id,
                 "status": "success"},
        status_code=status.HTTP_200_OK
    )

# HTML
@router.get("/html/{item_id}",response_class=HTMLResponse)
def html_response(item_id: int):
    html_str=f'''
    <html>
        <body>
            <h1>HTML Response</h1>
            <p>Item ID: {item_id}</p>
            <p>Status: success</p>
        </body>
    </html>
    '''
    return HTMLResponse(
        content=html_str,
        status_code=status.HTTP_200_OK
    )

# Redirect
@router.post("/create_redirect")
def redirect_response(item_id: int= Form(), item_name: str= Form()):    
    # Login (Post) -> Redirect -> Main Page (Get) : 302 : Method가 바뀔 때
    print(f"item_id: {item_id}, item_name: {item_name}")

    # Method가 바뀌면 STATUS는 302 / default 307은 Method가 안바뀜
    return RedirectResponse(
        url=f"/response/response/html/{item_id}",
        status_code=status.HTTP_302_FOUND
    )

