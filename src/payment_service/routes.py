"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .schemas import ProcessPaymentRequest, ProcessPaymentResponse
from .service import process_payment

router = APIRouter()


@router.post("/payments/process", response_model=ProcessPaymentResponse, status_code=200)
def process_payment_route(req: ProcessPaymentRequest) -> ProcessPaymentResponse:
    result = process_payment(
        order_id=req.order_id,
        amount=req.amount,
        currency=req.currency,
        payment_method=req.payment_method,
    )
    return ProcessPaymentResponse(
        transaction_id=result["transaction_id"],
        status=result["status"],
        processed_at=result["processed_at"],
    )
