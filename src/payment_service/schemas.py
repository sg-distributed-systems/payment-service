from pydantic import BaseModel


class ProcessPaymentRequest(BaseModel):
    order_id: str


class ProcessPaymentResponse(BaseModel):
    success: bool
