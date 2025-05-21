from fastapi import FastAPI
from app.api.v1.routes import router as v1_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version=settings.app_version
)

API_PREFIX_V1 = "/api/v1"
app.include_router(v1_router, prefix=API_PREFIX_V1)
