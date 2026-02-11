from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def health():
    return {"status": "up", "service": "bizsync-ai"}
