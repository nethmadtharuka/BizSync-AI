from fastapi import APIRouter, Request, Query
from app.core.config import settings

router = APIRouter()

@router.get("/webhooks/whatsapp")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):
    if hub_mode == "subscribe" and hub_verify_token == settings.WHATSAPP_VERIFY_TOKEN:
        return int(hub_challenge)
    return {"error": "verification failed"}

@router.post("/webhooks/whatsapp")
async def receive_whatsapp(request: Request):
    data = await request.json()
    print("WHATSAPP EVENT:", data)
    return {"status": "received"}
