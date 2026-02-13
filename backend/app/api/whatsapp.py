from fastapi import APIRouter, Request, Query, Depends
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.db import get_db
from app.models.business import Business
from app.models.customer import Customer
from app.models.message import Message

router = APIRouter()

@router.get("/webhooks/whatsapp")
async def verify_webhook(
    hub_mode: str = Query(None, alias="hub.mode"),
    hub_verify_token: str = Query(None, alias="hub.verify_token"),
    hub_challenge: str = Query(None, alias="hub.challenge"),
):
    """Webhook verification (Meta calls this once during setup)"""
    if hub_mode == "subscribe" and hub_verify_token == settings.WHATSAPP_VERIFY_TOKEN:
        return int(hub_challenge)
    return {"error": "verification failed"}

@router.post("/webhooks/whatsapp")
async def receive_whatsapp(request: Request, db: Session = Depends(get_db)):
    """Receive incoming WhatsApp messages"""
    data = await request.json()
    print("WHATSAPP EVENT:", data)

    # For MVP: assume one business (create if missing)
    biz = db.query(Business).first()
    if not biz:
        biz = Business(name="BizSync AI Demo Store")
        db.add(biz)
        db.commit()
        db.refresh(biz)  # Get the auto-generated ID

    # Extract phone number and message text from WhatsApp payload
    phone = None
    text = None
    try:
        entry = data["entry"][0]
        changes = entry["changes"][0]["value"]
        messages = changes.get("messages", [])
        if messages:
            phone = messages[0]["from"]  # Customer's phone number
            text = messages[0].get("text", {}).get("body")  # Message text
    except Exception:
        pass  # If payload structure is different, skip silently

    # Save to database if we got a phone number
    if phone:
        # Find or create customer
        customer = db.query(Customer).filter(
            Customer.business_id == biz.id,
            Customer.phone == phone
        ).first()
        
        if not customer:
            customer = Customer(business_id=biz.id, phone=phone)
            db.add(customer)
            db.commit()
            db.refresh(customer)

        # Save message
        msg = Message(
            business_id=biz.id,
            customer_id=customer.id,
            direction="IN",
            text=text
        )
        db.add(msg)
        db.commit()

    return {"status": "received"}