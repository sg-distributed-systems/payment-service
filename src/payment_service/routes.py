"""
API route definitions for the service.

Defines FastAPI router endpoints that handle incoming HTTP requests and
delegate to core business logic functions.
"""
from fastapi import APIRouter

from .main import process_payment
from .schemas import ProcessPaymentRequest, ProcessPaymentResponse

router = APIRouter()


@router.post("/payments/process", response_model=ProcessPaymentResponse)
def process_payment_route(req: ProcessPaymentRequest) -> ProcessPaymentResponse:
    result = process_payment(req.order_id)
    return ProcessPaymentResponse(success=result)
