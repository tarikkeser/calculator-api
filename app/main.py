from fastapi import FastAPI
from app.api.v1.route import router as v1_router
from app.api.v2.route import router as v2_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

API_PREFIX_V1 = "/api/v1"
API_PREFIX_V2 = "/api/v2"

app.include_router(v1_router, prefix=API_PREFIX_V1)
app.include_router(v2_router, prefix=API_PREFIX_V2)
