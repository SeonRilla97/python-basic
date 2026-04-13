from fastapi import APIRouter
from . import jinja

router = APIRouter(
    prefix="/template",
    tags=["template"]
)

route_mappings = [
    (jinja.router, ""),
]

for sub_router, sub_prefix in route_mappings:
    router.include_router(sub_router, prefix=sub_prefix)