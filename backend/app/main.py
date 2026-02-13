from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router
from app.api.whatsapp import router as whatsapp_router
from app.core.config import settings

app = FastAPI(title=settings.APP_NAME)

# Add CORS middleware ⬇️
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(health_router, prefix="/api")
app.include_router(whatsapp_router, prefix="/api")

@app.get("/")
def root():
    return {"ok": True, "service": "bizsync-ai"}