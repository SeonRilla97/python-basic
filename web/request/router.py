from fastapi import APIRouter
from . import path_param, query_param, body, form, request


router = APIRouter(
    prefix="/request" # 공통 경로
)

# [리팩토링] 라우터 객체와 경로를 리스트로 매핑하여 일괄 등록
route_mappings = [
    (path_param.router, "/path"),
    (query_param.router, "/query"),
    (body.router, "/body"),
    (form.router, "/form"),
    (request.router, "/request"),
]

for sub_router, sub_prefix in route_mappings:
    router.include_router(sub_router, prefix=sub_prefix, tags=["request"])