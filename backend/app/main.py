from fastapi import FastAPI
from app.api.health import router as health_router
from app.api.whatsapp import router as whatsapp_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(health_router, prefix="/api")
app.include_router(whatsapp_router, prefix="/api")

@app.get("/")
def root():
    return {"ok": True, "service": "bizsync-ai"}
